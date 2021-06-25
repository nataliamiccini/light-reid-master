import os
from .reid_samples import ReIDSamples

'''img1123'''
class OriginalImages_ReID(ReIDSamples):
   
    dataset_url = 'http://188.138.127.15:81/Datasets/Market-1501-v15.09.15.zip'

    def __init__(self, data_path, combineall=False, download=False):

        # is not exist and download true, download dataset or stop
        if not os.path.exists(data_path):
            if download:
                print('dataset path {} is not existed, start download dataset'.format(data_path))
                self.download_dataset(data_path, self.dataset_url)
            else:
                return 'dataset path {} is not existed, start download dataset'.format(data_path)

        # paths of train, query and gallery
        train_path = os.path.join(data_path, 'Img-train/')
        query_path = os.path.join(data_path, 'query/')
        gallery_path = os.path.join(data_path, 'gallery/')

        # load samples
        train = self._load_samples(train_path)
        query = self._load_samples(query_path)
        gallery = self._load_samples(gallery_path)
        
        # init
        super(OriginalImages_ReID, self).__init__(train, query, gallery, combineall)

    def _load_samples(self, folder_dir):
        '''return (img_path, identity_id, camera_id)'''
        samples = []
        root_path, _, files_name = self.os_walk(folder_dir)
        for file_name in files_name:
            if '.jpg' in file_name:
                person_id = self._analysis_file_name(file_name)
                samples.append([root_path+file_name, person_id])
        return samples

    def _analysis_file_name(self, file_name):
        '''
        :param file_name: format like 0844_c3s2_107328_01.jpg
        :return: 0844, 3
        '''
        split_list = file_name.replace('.jpg', '').split('-')
        person_id = int(split_list[0])
        return person_id



