import os
import urllib.request
from datetime import datetime
import time

image_url = "http://192.168.86.28/capture"


def save_image(image_data, sample_timestamp):
    sample_datetime = datetime.utcfromtimestamp(sample_timestamp)
    folder_date_string = sample_datetime.strftime('%Y-%m-%d')
    file_date_string = folder_date_string + \
        '_at_' + sample_datetime.strftime('%H-%M-%S')
    folder_path = f"./{folder_date_string}-UTC/"
    file_path = f"{file_date_string}-UTC.jpg"
    full_path = folder_path + file_path

    print("Saving image to: ", full_path)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(full_path, 'wb') as file:
        file.write(image_data)


def main():
    while True:
        try:

            # record timestamp of image sample
            sample_timestamp = datetime.now().timestamp()

            # download image
            response = urllib.request.urlopen(image_url)
            image_data = response.read()

            save_image(image_data, sample_timestamp)
        except KeyboardInterrupt:
            print("Stopped capturing images.")
            break
        except Exception as e:
            print("Error fetching image: " + e)

#        time.sleep(1)


if __name__ == "__main__":
    main()
