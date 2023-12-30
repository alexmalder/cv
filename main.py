import cv2

vidcap = cv2.VideoCapture('videos/dont-try-it.mp4')
success,image = vidcap.read()
count = 0

while success:
  cv2.imwrite("images/dont-try-it/frame-%d.jpg" % count, image)
  success, image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
