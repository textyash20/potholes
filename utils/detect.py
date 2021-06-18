import numpy as np
from utils import detector_util, save_image
import cv2

import constants
from database import db


def detect_pothole(path, latitude, longitude, user_email_session):
    lat = latitude
    lon = longitude
    img = path

    score_trash = 0.50
    detection_graph = constants.detection_graph
    sess = constants.sess
    num_potholes_detect = 100
    print("entering Pothole Detect  method")
    im_height, im_width = (None, None)
    while True:
        frame = cv2.imread(img)
        frame = np.array(frame)
        new_lat = lat
        new_lon = lon

        if im_height == None:
            im_height, im_width = frame.shape[:2]

        # Passing image through tensorflow model

        boxes, scores, classes = detector_util.detect_objects(frame, detection_graph, sess)

        # drawing bbox on image
        pothole_cnt = detector_util.draw_box_on_image(num_potholes_detect, score_trash, scores, boxes, classes, im_width,
                                            im_height, frame, lat, lon)
        print(str(pothole_cnt) + ' Potholes found ')
        print('before writing image')

        if pothole_cnt != 0:
            try:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                print('inside image saving')
                try:
                    img_path_save, image_name_save = save_image.get_save_location_of_detected()
                    cv2.imwrite(img_path_save, frame)
                    print('done saving')
                    db.savei(user_email_session, image_name_save, img_path_save, new_lat, new_lon, pothole_cnt)
                except:
                    print("Can't Save image")
                    pass

                return img_path_save, pothole_cnt
            except:
                return 0
        else:
            return 0
