import numpy as np
import cv2
import os

def add_object(objDict, newObj):
    if newObj in objDict.keys():
        # Object already exists
        objDict[newObj] += 1
    else: objDict[newObj] = 1

    return objDict

def scan_image(imagePath, libPath, showImage=False, confidence=0.5, threshold=0.3):
    objects = {}
    args = {}
    args['image'] = imagePath
    args['yolo'] = libPath
    args['confidence'] = confidence
    args['threshold'] = threshold

    # Load COCO Class Labels our YOLO Model was trained on
    labelsPath = os.path.sep.join([args["yolo"], "coco.names"])
    LABELS = open(labelsPath).read().strip().split("\n")

    # Init list of colors to represent possible class labels
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

    # Derive paths to YOLO Weights and model configuration
    weights = os.path.sep.join([args["yolo"], "yolov3.weights"])
    config = os.path.sep.join([args["yolo"], "yolov3.cfg"])

    # Load YOLO Object Detector trained on COCO dataset - 80 classes
    net = cv2.dnn.readNetFromDarknet(config, weights)

    image = cv2.imread(args["image"]) # Load Input Image
    (H, W) = image.shape[:2]

    # Determine Output Layer names needed from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Construct Blob according to input image
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln) # Get Layer Outputs

    boxes = []
    confidences = []
    classIDs = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores) # Get Class ID
            confidence = scores[classID]

            # Filter out Trash Detections
            if confidence > args["confidence"]:
                # Scale the bounding box to the size of image
                box = detection[0 : 4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # Get Coordinates of bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # Update arrays
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)


    # Apply non-maxima suppression - Suppresses weak, overlapping bounding boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"], args["threshold"])

    # Draw only if there is at least one detection
    if len(idxs) > 0:
        print("PRINTING OBJECTS WITH CONFIDENCE LEVEL...")
        for i in idxs.flatten():
            # Get Bounding Boxes
            objName = LABELS[classIDs[i]]
            objects = add_object(objects, objName)
            text = "{}: {:.4f}".format(objName, confidences[i])
            print(text)

            if (showImage):
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                color = [int(c) for c in COLORS[classIDs[i]]]
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        print("DONE PRINTING OBJECTS WITH CONFIDENCE LEVEL...")


    # Show Output image
    if (showImage):
        cv2.imshow("Image", image)
        cv2.waitKey(0)

    return objects
