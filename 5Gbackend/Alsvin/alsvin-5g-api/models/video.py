from sqlalchemy.ext.hybrid import hybrid_property

from alsvin-5g-api.extensions import db, pwd_context


class Video(db.Model):
    """Basic user model"""

    id = db.Column(db.Integer, primary_key=True)
    videoHash = db.Column(db.Text, unique=True, nullable=False)
    video = db.Column("video", db.LargeBinary, nullable=False)

    @hybrid_property
    def video(self):
        return self.video

    @video.setter
    def video(self, value):
        self.video = pwd_context.hash(value)

    @videoHash.setter
    def videoHash(self, value):
        self.videoHash = pwd_context.hash(value)

    def __repr__(self):
        return "<Video %s>" % self.videoHash
