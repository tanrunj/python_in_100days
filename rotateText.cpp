#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>
using namespace std;
using namespace cv;
#define PI 3.14159265

// Arrow Attributes
int ARROWLENGTH = 15;
int ARROWANGLE = 25; 
Scalar ARROWCOLOR1 = Scalar(0, 220, 0);
Scalar ARROWCOLOR2 = Scalar(0, 0, 220);
int LINETHICKNESS = 1;
int LINETYPE = 8;   //严格使用８连接线，谨慎使用CV_AA！ 插值算法会导致基于颜色的碰撞检测出现Bug!

// Font Attributes
int FONTFACE = FONT_HERSHEY_COMPLEX;
double FONTSCALE = 0.5;
Scalar FONTCOLOR = Scalar(0, 0, 0);
int FONTTHICKNESS = 1;


void rotateImage(const cv::Mat &srcImg, cv::Mat &rotatedImg, double angle, cv::Scalar filled_color)
{

	int h = srcImg.rows;
	int w = srcImg.cols;

	//求对角线的长度，做一个以对角线为边长的正方形图像
	int diaLength = int(sqrt((h*h + w*w)));
	cv::Mat tempImg(diaLength, diaLength, srcImg.type(), filled_color);//filled_color 边缘填充的颜色
	int tx = diaLength / 2 - w / 2;//原图左上角在新图上的x坐标  
	int ty = diaLength / 2 - h / 2;//原图左上角在新图上的y坐标  
	srcImg.copyTo(tempImg(cv::Range(ty, ty + h), cv::Range(tx, tx + w)));//把原图先复制到新的临时图上。

	//以新的临时图的中心点为旋转点
	cv::Point rotatepoint;
	rotatepoint.x = rotatepoint.y = diaLength / 2;
	cv::Mat rotaMat = getRotationMatrix2D(rotatepoint, angle, 1); // 获取二维旋转的仿射变换矩阵  
	warpAffine(tempImg, rotatedImg, rotaMat, cv::Size(diaLength, diaLength), 1, cv::BORDER_CONSTANT, cv::Scalar(255, 255, 255));//进行仿射变换
	threshold(rotatedImg, rotatedImg, 128, 255, THRESH_BINARY);
	return;
}


void putTextWithAngle( cv::Mat& img, const std::string& text, cv::Point org, float angle=0.0, int fontFace=FONTFACE, double fontScale=FONTSCALE, Scalar color=FONTCOLOR, int thickness = FONTTHICKNESS, int lineType = LINETYPE, bool bottomLeftOrigin = false )
{
    int sign = -1;
    if( fmod(angle,180.0)/90)
        sign = 1;
    if (angle!=90 && angle!=-90)
        angle = sign * fmod(angle,90.0);

	cv::Size text_size = cv::getTextSize(text, fontFace, fontScale, thickness, int());//文本的boundingbox大小
	cv::Mat text_mat(text_size.height + 10, text_size.width + 10, CV_8UC3, cv::Scalar(255, 255, 255));//创建文字图像，大小加10是为了保证文本位置足够完全显示，不会被边缘裁剪
	cv::putText(text_mat, text, cv::Point(5, text_mat.rows - 5), fontFace, fontScale, color, thickness, lineType);//添加文字到文字图像
    cv::Mat rotate_image;
	rotateImage(text_mat, rotate_image, angle, cv::Scalar(255, 255, 255));//得到旋转后的文字图像
	
	
	
	// 基于颜色的碰撞检测算法
	// 根据方向添加文字的备选位置
	vector<Point> directions;
	int margin = 5;
    int scale = 3;
	double sections = double(scale*2);

    double dRot = angle * PI /180;
	double dSin = sin(dRot);
	double dCos = cos(dRot);
	//　确认沿靠尺方向偏移　
	directions.push_back(Point(0,0));
	for(int i=1; i<=sections; i++)
		directions.push_back(Point( -(scale * text_size.width * (i/sections) + margin)*dCos , (scale * text_size.width * (i/sections) + margin)*dSin ));
	for(int i=1; i<=sections; i++)	
		directions.push_back(Point( (scale * text_size.width * ( i/sections) + margin)*dCos ,  -(scale * text_size.width * ( i/sections) + margin)*dSin ));

	

	// 基于颜色的碰撞检测
	Point newOrigin;
	bool find_empty = false;
	for(vector<Point>::iterator pit=directions.begin(); pit!=directions.end(); ++pit)
	{
		newOrigin = org + (*pit);
		// 判断新位置是否超出图像大小
		if( (newOrigin.x-text_size.width)<0 || (newOrigin.x+text_size.width)>img.cols 
          || (newOrigin.y - text_size.height)< 0 || (newOrigin.y +text_size.height) > img.rows)
			continue;
		bool collision = false;
		// 基于颜色判断
		for(int i = newOrigin.x - text_size.width/2; i < newOrigin.x +  text_size.width/2 ; i++)
		{
			for(int j = newOrigin.y - text_size.height/2; j<newOrigin.y + text_size.height/2; j++)
			{
				// 对仿射变形后的点进行碰撞检测
				double x = i*dCos - j*dSin + newOrigin.x  * (1-dCos) + newOrigin.y *dSin;
				double y = i*dSin + j*dCos - newOrigin.x  * dSin + newOrigin.y * (1-dCos);				
				if (Scalar(img.at<Vec3b>(y,x)) == FONTCOLOR)
				{
					collision = true;
					break;
				}	
			}
			if(collision)
				break;
		}
		if(!collision)
		{
			find_empty = true;
			break;
		}
	}
	// 若不存在空位，则用原来的位置。
	if(!find_empty)
		newOrigin = org;

	// 确认位置，画图
    int rectX = newOrigin.x -rotate_image.cols/2;
    if(rectX<0)
        rectX = 0;
    if(newOrigin.x + rotate_image.cols/2 >img.cols)
        rectX = img.cols - rotate_image.cols;

    int rectY = newOrigin.y-rotate_image.rows/2;
    if(rectY<0)
        rectY = 0;
    if(newOrigin.y + rotate_image.rows/2 > img.rows)
        rectY = img.rows - rotate_image.rows;
   
	cv::Mat roi = img(cv::Rect( rectX, rectY , rotate_image.cols, rotate_image.rows));
	// 按位运算，逻辑and,相当于取两图相同位置像素较小值
    roi = (roi & rotate_image);

	roi.release();
	rotate_image.release();
	text_mat.release();
}



int main()
{
    Mat image = imread("/home/abc/Desktop/project/1.bmp", 1);
    Mat element5(5,5,CV_8U, Scalar(1));
	Mat open;
	morphologyEx(image, open, MORPH_OPEN, element5);


	// Test Case 1: Point数值越界
    string textR1 = "R1:0.30";
	putTextWithAngle( open, textR1, Point(-300,-3300), 90.0);
    putTextWithAngle( open, textR1, Point(2200,700), 90.0);

    
    // Test Case 2: 负角度摆尺，同位置堆叠
    string textR2 = "R2:0.00";
	putTextWithAngle( open, textR2, Point(550,400), -20.0);
	putTextWithAngle( open, textR2, Point(550,400), -20.0);
    putTextWithAngle( open, textR2, Point(550,400), -20.0);
    putTextWithAngle( open, textR2, Point(550,400), -20.0); 


    // Test Case 3: 大角度摆尺，相邻位置堆叠，且接近图像边界
    string textR3 = "R3:0.20";
    putTextWithAngle( open, textR3, Point(700,700), 405.0);
    putTextWithAngle( open, textR3, Point(700,700), 405.0);
    putTextWithAngle( open, textR3, Point(700,700), 405.0);
    putTextWithAngle( open, textR3, Point(800,800), 405.0);
    putTextWithAngle( open, textR3, Point(850,850), 405.0);

    // Test Case 4: 相同位置相交摆尺
    string textR4 = "R4:0.90";
    putTextWithAngle( open, textR4, Point(300,300), 45.0);

    putTextWithAngle( open, textR4, Point(300,300), -45.0);
    textR4 = "R4:0.95";
    putTextWithAngle( open, textR4, Point(320,320), 45.0);

    // putTextWithAngle( open, textR4, Point(320,320), -45.0); //

    // Test Case 5: 相邻相交摆尺
    string textR5 = "R5:1.35";

    putTextWithAngle( open, textR5, Point(200,600), 30.0);
    putTextWithAngle( open, textR5, Point(200,600), 45.0);
    putTextWithAngle( open, textR5, Point(200,600), 60.0);
    putTextWithAngle( open, textR5, Point(200,600), 75.0);

    cv::imshow("open", open);

	cv::waitKey(0);
	return 0;
}
   