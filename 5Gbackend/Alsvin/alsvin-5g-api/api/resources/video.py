from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from alsvin-5g-api.api.schemas import VideoSchema
from alsvin-5g-api.models import Video
from alsvin-5g-api.extensions import db
from alsvin-5g-api.commons.pagination import paginate


class VideoResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      summary: Get a video
      description: Get a single video by ID
      parameters:
        - in: path
          name: video_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  video: VideoSchema
        404:
          description: video does not exists
    put:
      tags:
        - api
      summary: Update a video
      description: Update a single video by ID
      parameters:
        - in: path
          name: video_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              VideoSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: video updated
                  video: VideoSchema
        404:
          description: video does not exists
    delete:
      tags:
        - api
      summary: Delete a video
      description: Delete a single video by ID
      parameters:
        - in: path
          name: video_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: video deleted
        404:
          description: video does not exists
    """

    method_decorators = [jwt_required()]

    def get(self, video_id):
        schema = VideoSchema()
        video = Video.query.get_or_404(video_id)
        return {"video": schema.dump(video)}

    def put(self, video_id):
        schema = VideoSchema(partial=True)
        video = Video.query.get_or_404(video_id)
        video = schema.load(request.json, instance=video)

        db.session.commit()

        return {"msg": "video updated", "video": schema.dump(video)}

    def delete(self, video_id):
        video = Video.query.get_or_404(video_id)
        db.session.delete(video)
        db.session.commit()

        return {"msg": "video deleted"}


class VideoList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - api
      summary: Get a list of videos
      description: Get a list of paginated videos
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/VideoSchema'
    post:
      tags:
        - api
      summary: Create a video
      description: Create a new video
      requestBody:
        content:
          application/json:
            schema:
              VideoSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: video created
                  video: VideoSchema
    """

    method_decorators = [jwt_required()]

    def get(self):
        schema = VideoSchema(many=True)
        query = Video.query
        return paginate(query, schema)

    def post(self):
        schema = VideoSchema()
        video = schema.load(request.json)

        db.session.add(video)
        db.session.commit()

        return {"msg": "video created", "video": schema.dump(video)}, 201
