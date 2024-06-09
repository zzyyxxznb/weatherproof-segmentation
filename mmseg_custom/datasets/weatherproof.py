from mmseg.datasets.builder import DATASETS
from mmseg.datasets.custom import CustomDataset

@DATASETS.register_module()
class weatherproof(CustomDataset):
      CLASSES = ('background','building','other-structure','road','sky','stone',
                'terrain-grass','terrain-other','terrain-snow','tree'),
      PALETTE=[[9,9,9] ,[0, 0, 0], [1, 1, 1], [2, 2, 2],
                [3, 3, 3], [4, 4, 4], [5, 5, 5],
                [6, 6, 6], [7, 7, 7], [8, 8, 8]]
  

      def __init__(self, **kwargs):
        super(weatherproof, self).__init__(
          img_suffix='.png',
          seg_map_suffix='.png',
          reduce_zero_label=False,
          **kwargs)
