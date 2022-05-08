# coding: utf-8
#from sqlalchemy import Column, db.DateTime, db.Float, db.ForeignKey, db.Integer, db.String, db.Table
#from sqlalchemy.orm import db.relationship
from sqlalchemy.ext.declarative import declarative_base
from routes import db

class Serializer(object):
    def to_dict(self):
        """
        Jsonify the sql alchemy query result.
        """
        convert = dict()
        # add your coversions for things like datetime's
        # and what-not that aren't serializable.
        d = dict()
        for c in self.__table__.columns:
            v = getattr(self, c.name)
            if c.type in convert.keys() and v is not None:
                try:
                    d[c.name] = convert[c.type](v)
                except:
                    d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
            elif v is None:
                d[c.name] = str()
            else:
                d[c.name] = v
        return d



t_actor_participants = db.Table(
    'actor_participants', db.metadata,
    db.Column('actor_id', db.ForeignKey(u'actors.id'), primary_key=True, nullable=False),
    db.Column('participant_id', db.ForeignKey(u'participants.id'), primary_key=True, nullable=False, index=True)
)


class Actor(db.Model, Serializer):
    __tablename__ = 'actors'

    id = db.Column(db.String(20), primary_key=True)
    role = db.Column(db.String(63))

    participants = db.relationship(u'Participant', secondary='actor_participants')


class Answer(db.Model, Serializer):
    __tablename__ = 'answers'

    id = db.Column(db.String(20), primary_key=True)
    assessor_actor_id = db.Column(db.ForeignKey(u'actors.id'), index=True)
    assessee_actor_id = db.Column(db.ForeignKey(u'actors.id'), index=True)
    assessee_artifact_id = db.Column(db.ForeignKey(u'artifacts.id'), index=True)
    criterion_id = db.Column(db.ForeignKey(u'criteria.id'), index=True)
    evaluation_mode_id = db.Column(db.ForeignKey(u'eval_modes.id'), index=True)
    comment = db.Column(db.String)
    comment2 = db.Column(db.String)
    rank = db.Column(db.Integer)
    score = db.Column(db.Float)
    create_in_task_id = db.Column(db.ForeignKey(u'tasks.id'), index=True)
    submitted_at = db.Column(db.DateTime)

    assessee_actor = db.relationship(u'Actor', primaryjoin='Answer.assessee_actor_id == Actor.id')
    assessee_artifact = db.relationship(u'Artifact')
    assessor_actor = db.relationship(u'Actor', primaryjoin='Answer.assessor_actor_id == Actor.id')
    create_in_task = db.relationship(u'Task')
    criterion = db.relationship(u'Criterion')
    evaluation_mode = db.relationship(u'EvalMode')


class Artifact(db.Model, Serializer):
    __tablename__ = 'artifacts'

    id = db.Column(db.String(20), primary_key=True)
    content = db.Column(db.String)
    elaboration = db.Column(db.String)
    submitted_in_task_id = db.Column(db.ForeignKey(u'tasks.id'), index=True)
    context_case = db.Column(db.String(255))

    submitted_in_task = db.relationship(u'Task')


class Criterion(db.Model, Serializer):
    __tablename__ = 'criteria'

    id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    type = db.Column(db.String(63))
    min_score = db.Column(db.Float)
    max_score = db.Column(db.Float)
    weight = db.Column(db.Float)


class EvalMode(db.Model, Serializer):
    __tablename__ = 'eval_modes'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))


t_items = db.Table(
    'items', db.metadata,
    db.Column('id', db.String(20)),
    db.Column('content', db.String),
    db.Column('reference_id', db.String(20)),
    db.Column('type', db.String(63))
)


class Participant(db.Model, Serializer):
    __tablename__ = 'participants'

    id = db.Column(db.String(20), primary_key=True)
    app_name = db.Column(db.String(255))


class Task(db.Model, Serializer):
    __tablename__ = 'tasks'

    id = db.Column(db.String(20), primary_key=True)
    task_type = db.Column(db.String(63))
    task_description = db.Column(db.String(255))
    starts_at = db.Column(db.DateTime)
    ends_at = db.Column(db.DateTime)
    assignment_title = db.Column(db.String(255))
    course_title = db.Column(db.String(255))
    organization_title = db.Column(db.String(255))
    owner_name = db.Column(db.String(255))
    cip_level1_code = db.Column(db.String(255))
    cip_level2_code = db.Column(db.String(255))
    cip_level3_code = db.Column(db.String(255))
    app_name = db.Column(db.String(255))
