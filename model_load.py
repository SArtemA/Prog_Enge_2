from ultralytics import YOLO
import gdown
gdown.download(url='https://drive.google.com/file/d/1nolYX5CFPJWp8BcyPscUp-urKQ3jTTf-/view?usp=drive_link', fuzzy=True)
model = YOLO('best.pt')
