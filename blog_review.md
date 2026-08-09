Blog Review: The mechanics of recognizing facial emotion via MediaPipe.
When it comes to the mechanics of recognizing emotional responses, I find the underlying system of Google's MediaPipe-an open-source ML system-to be really interesting. In order to determine an emotion from a raw image, the process can actually be divided into four mathematical-based stages.

Stage 1: Map the Face.
The system uses Face Mesh-a 3D graphing device that can detect 468 specific facial landmarks in a millisecond-as its base. The algorithm basically scans the photo, extracts the face, and throws the background away. As this 468-dot grid represents specific points on the face, each point has three coordinates, X, Y, and Z. With this increasing accuracy with number of dots, the image generates a 1404 (468*3) mathematically derived number representing the face itself.

Stage 2: Normalize the Face.
Because the image given to the system can vary by distance, size, and angel-the algorithm has to make it more uniform and stable. Using a transformation matrix(the equivalent of rotating, scaling and translating), the system centers the faces at a single spot making its orientation and size identical. An interesting feature that this system has to offer is it actually does not save the actual image, only the 1404 number is kept, meaning that your privacy is safe.

Stage 3: Feature Extraction.
Once all the 1404 points are extracted the system then finds the emotion in one of three ways:

The Ruler Method (Action Units). This looks for minute muscle movements across the face that combine to form expressions but cannot identify movement from forehead.

Deep Learning (Raw Coordinates). This sends all the 1404 points to a neural net where it essentially uses a "difference vector," which takes a person's base neutral face and finds out the difference in the coordinates of their emotional face from their neutral face. This eliminates base facial characteristics.

Blendshapes. This is Google's in-house method to overcome vector complexities-it has trained it's system on millions of faces allowing it to provide the level of each of the 52 basic expressions directly.

Stage 4: Classification.
After finding the emotion based on the data collected, the final stage is to classify this emotion as "Happy" for example. Traditional ML methods can be used like a Random Forest model, which is essentially a bunch of sequential yes/no decisions, or an SVM or Support Vector Machine that draw boundaries, meaning if the smile value is higher with more eye squinting that implies shock or happiness while a medium value with only a smile implies anger. More advanced networks like a CNN or GNN network can also do this, and are able to learn these complex layer networks independently to provide the exact classification.