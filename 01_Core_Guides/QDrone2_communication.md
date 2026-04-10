# Python Section of QDrone2 Communication Channels and Ports

if useCameras:

    realsense = Camera3D(deviceId="0@tcpip://localhost:18986",
                        mode='RGB&DEPTH',
                        frameWidthRGB=640,
                        frameHeightRGB=480,
                        frameRateRGB=frameRate,
                        frameWidthDepth=640,
                        frameHeightDepth=480,
                        frameRateDepth=frameRate,
                        readMode=0)
 
    camRight = Camera2D(cameraId="0@tcpip://localhost:18982",
                    frameWidth=640, frameHeight=480,
                    frameRate=frameRate)
 
    camBack = Camera2D(cameraId="1@tcpip://localhost:18983",
                    frameWidth=640, frameHeight=480,
                    frameRate=frameRate)
 
    camLeft = Camera2D(cameraId="2@tcpip://localhost:18984",
                        frameWidth=640, frameHeight=480,
                        frameRate=frameRate)
 
    camDown = Camera2D(cameraId="3@tcpip://localhost:18985",
                    frameWidth=640, frameHeight=480,
                    frameRate=frameRate)
 

Ports:

    dataStream = BasicStream('tcpip://localhost:18373',
                       agent='C', sendBufferSize=1460,
                       receiveBuffer=np.zeros((1,16), dtype=np.float64),
                       recvBufferSize=1460, nonBlocking=False)
 
    gameStream = BasicStream('tcpip://127.0.0.1:19001',
                       agent='C', sendBufferSize=8,
                       receiveBuffer=np.zeros((1,1), dtype=np.float64),
                       recvBufferSize=24, nonBlocking=False)

#### Back to: [Operational Guide ](../01_Core_Guides/Operational_Guide.md)
