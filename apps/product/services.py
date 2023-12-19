import os


def get_product_photo_upload_path(instance, filename):
    product_name = instance.product.name
    upload_path = os.path.join('product_photos', product_name, filename)
    return upload_path
