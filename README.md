## Parsing of images for DL

Here is one of the parsers I've created in order to scrape images of clothing from Bonprix.de web-site. These images were intended to train DL model for try-on of clothing. 
The dataset can be found [here](https://disk.yandex.ru/d/PeBWMc8BU0uIAQ):



Overall I succesfully performed the scrapping part of bonprix.de web-page (including dresses), then manually cleaned the data by removing images with back pose and fragmented products based on their order on web-site (from 6903 lower body images only 3644 were left, from 17244 upper body images only 8669 were left, from 9542 dresses 4794 images were left).

I have tried pose estimation in order to remove other pose outliers - images, where person is not in strictly in front position, and achieved the needed result: distance between vectors of pose points can tell the difference between acceptable and not acceptable images. This you can see in Jupyter Notebook attached.

By examining the data, I have encountered other data imperfections. One of them is when on the cloth picture there are few products instead of one. In order to get rid of such images I would calculate the mean white space percentage on good images (where only one product is shown) to set a threshold per category, and compare it to the white space percentage of each image. Logically, images with several product on them will show a different ratio (they will have less white space).

![image](https://github.com/exxyyf/data_collection_for_dl/assets/118925388/d04b2d01-ed23-45cf-a9bb-ca6550540a76)

![image](https://github.com/exxyyf/SCP_data_collection/assets/118925388/386812e5-b8aa-4750-b6e4-aa888577d52e)

