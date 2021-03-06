import sqlalchemy as sa
from sqlalchemy import types
from sqlalchemy.dialects import postgresql as pg

from sqlalchemy.ext.declarative import declarative_base

metadata = sa.MetaData()
Base = declarative_base(metadata=metadata)


class Tweet(Base):
    __tablename__ = 'tweet'
    __table_args__ = (
        sa.UniqueConstraint('tweet_id', 'collection', name='uix_tweet_tweet_id'),
        sa.Index('idx_tweet_collection', 'collection'),
        sa.Index('idx_tweet_created_at', 'created_at')
    )

    _id = sa.Column(types.Integer, primary_key=True)

    tweet_id = sa.Column(types.BigInteger, nullable=False)
    collection = sa.Column(types.String, nullable=False)

    # tweet = Column(pg.JSONB, nullable=False)
    label = sa.Column(types.String)
    features = sa.Column(pg.JSONB)

    created_at = sa.Column(types.DateTime, nullable=False)

indexes = [
    sa.Index(
        'idx_tweet_features_screen_names',
        Tweet.features['screen_names'],
    ),

    sa.Index(
        'idx_tweet_features_user_mentions',
        Tweet.features['user_mentions'],
    ),

    sa.Index(
        'idx_tweet_features_hashtags',
        Tweet.features['hashtags'],
    ),

    sa.Index(
        'idx_tweet_features_languages',
        Tweet.features['languages'],
    ),
]
