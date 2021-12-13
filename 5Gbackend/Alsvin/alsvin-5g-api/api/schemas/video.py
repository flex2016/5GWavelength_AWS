from alsvin-5g-api.models import Video
from alsvin-5g-api.extensions import ma, db

class VideoSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    video = ma.LargeBinary(load_only=True, required=True)

    class Meta:
        model = Video
        sqla_session = db.session
        load_instance = True