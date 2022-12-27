import csv
import os
import numpy as np
class creatcsv():  

   def __init__(self ,landmarks ,csvs_out_folder,pose_name) :
        self.landmarks = landmarks
        self.csvs_out_folder = csvs_out_folder
        self.pose_name=pose_name
        
   def creat(self) :
        
       # self.pose_class_names = sorted([n for n in os.listdir(self._images_in_folder) if not n.startswith('.')])

        if not os.path.exists(self.csvs_out_folder):
            os.makedirs(self.csvs_out_folder)

       # for pose_class_name in self.pose_class_names:
           # print('Bootstrapping ', pose_class_name, file=sys.stderr)

            # Paths for the pose class.
            #csv_out_path = os.path.join(self.csvs_out_folder, pose_class_name + '.csv')
        csv_out_path = os.path.join(self.csvs_out_folder,self.pose_name+ '.csv')
        with open(csv_out_path, 'w') as csv_out_file:
            csv_out_writer = csv.writer(csv_out_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            csv_out_writer.writerow([self.pose_name] + self.landmarks.flatten().astype(np.str).tolist())