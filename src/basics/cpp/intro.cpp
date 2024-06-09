#include <opencv2/core.hpp>
#include <openncv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>


#include <iostream>

int main() 
{
    std::string image_path = samples::findFile("starry_night.jpg");
    Mat img = imread(image_path, IMREAD_COLOR);

    if(img.empty())
    {
        std::count << "could not read the image: " << image_path  <<  std::endl;
        return 1;
    }

    imshow("Display window", img);
    int k = waitkey(0); 

    if(k == 's')
    {
        imwrite("starry_night.jpg", img);
    }

    return 0;

}