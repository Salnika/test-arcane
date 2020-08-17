from ma_config import ma


class GoodSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'name', 'description',
                  'good_type', 'city', 'room_nb', 'owner_name')


good_schema = GoodSchema()
goods_schema = GoodSchema(many=True)
