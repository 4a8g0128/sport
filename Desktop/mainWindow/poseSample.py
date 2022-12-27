import csv
import os
import numpy as np



class PoseSample(object):

  def __init__(self, name, landmarks, class_name, embedding):
    self.name = name
    self.landmarks = landmarks
    self.class_name = class_name
    self.embedding = embedding
     
class poencsv(object):
    def __init__(self,pose_samples_folder,
                fullbody,
                file_extension='csv',
                file_separator=',',
                n_landmarks=33,
                n_dimensions=3,
                top_n_by_max_distance=30,
                top_n_by_mean_distance=10, 
                axes_weights=(1., 1., 0.2)):
        self.full_boby = fullbody
        self._n_landmarks = n_landmarks
        self._n_dimensions = n_dimensions
        self._top_n_by_max_distance = top_n_by_max_distance
        self._top_n_by_mean_distance = top_n_by_mean_distance
        self._axes_weights = axes_weights
        self._pose_samples = self._load_pose_samples(pose_samples_folder,
                                                 file_extension,
                                                 file_separator,
                                                 n_landmarks,
                                                 n_dimensions,
                                                 fullbody)
    def _load_pose_samples(self,
                         pose_samples_folder,
                         file_extension,
                         file_separator,
                         n_landmarks,
                         n_dimensions,
                         fullbody):
        file_names = [name for name in os.listdir(pose_samples_folder) if name.endswith(file_extension)]

        pose_samples = []
        for file_name in file_names:
            # Use file name as pose class name.
            class_name = file_name[:-(len(file_extension) + 1)]
      
        # Parse CSV.
        with open(os.path.join(pose_samples_folder, file_name)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=file_separator)
            for row in csv_reader:
                assert len(row) == n_landmarks * n_dimensions + 1, 'Wrong number of values: {}'.format(len(row))
                landmarks = np.array(row[1:], np.float32).reshape([n_landmarks, n_dimensions])
                pose_samples.append(PoseSample(
                    name=row[0],
                    landmarks=landmarks,
                    class_name=class_name,
                    embedding=fullbody(landmarks),
          ))

        return pose_samples                                                 
    def __cell__(self, pose_landmarks):
        """Classifies given pose.
        Classification is done in two stages:
        * First we pick top-N samples by MAX distance. It allows to remove samples
            that are almost the same as given pose, but has few joints bent in the
            other direction.
        * Then we pick top-N samples by MEAN distance. After outliers are removed
            on a previous step, we can pick samples that are closes on average.
        
        Args:
        pose_landmarks: NumPy array with 3D landmarks of shape (N, 3).
        Returns:
        Dictionary with count of nearest pose samples from the database. Sample:
            {
            'pushups_down': 8,
            'pushups_up': 2,
            }
        """
           

        # Get given pose embedding.
        pose_landmarks = self.full_boby(pose_landmarks)
        flipped_pose_embedding = self.full_boby(pose_landmarks * np.array([-1, 1, 1]))

        # Filter by max distance.
        #
        # That helps to remove outliers - poses that are almost the same as the
        # given one, but has one joint bent into another direction and actually
        # represnt a different pose class.
        #max_dist_heap = []
        for sample_idx, sample in enumerate(self._pose_samples):
            max_dist = min(
            np.max(np.abs(sample.embedding - pose_landmarks) * self._axes_weights),
            np.max(np.abs(sample.embedding - flipped_pose_embedding) * self._axes_weights),
        )

        mean_dist = 100 -  round(max_dist)

        return mean_dist
  