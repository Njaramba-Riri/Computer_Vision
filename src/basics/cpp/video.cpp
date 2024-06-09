//Include libraries.
#include <opencv2/opencv.hpp>
#include <iostream>

//Namespace to nullify the use of cv::function sysntax.
using namespace std;
using namespace cv;

int main()
{
    //Initialize vid cap object.
    VideoCapture vid_capture("Images/cars.mp4");

    if (!vid_capture.isOpened())
    {
        cout << "Error opening video stream or file" << endl;
    }
    else
    {
        //Obtainn count and fps.
        int fps = vid_capture.get(5);
        cout << "Frames per Second: " << fps;         

        int frame_count = vid_capture.get(7);
        cout << "Frame count " << frame_count;
    }

    while(vid_capture.isOpened())
    {
        Mat frame;
        
        bool isSuccess = vid_capture.read(frame);

        if(isSuccess == true)
        {
            imshow("Frame", frame);
        }
        if(isSuccess == false)
        {
            cout << "Video is disconnected " << endl;
            break; 
        }

        int key = cv.waitKey(20);
        if(key == 'q')
        {
            cout << "q key is pressed, closing the video." << endl;
            break;
        }
    }
    vid_capture.release();
    cv.destroyAllWindow();
    return 0;
}
