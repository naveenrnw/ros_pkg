#include <termios.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>

#include <ros/ros.h>
#include <geometry_msgs/Twist.h>

#define KEYCODE_A 0x61
#define KEYCODE_D 0x64
#define KEYCODE_S 0x73
#define KEYCODE_W 0x77
#define KEYCODE_Q 0x71

class TeleopPR2Keyboard
{
  private:
  geometry_msgs::Twist cmd;

  ros::NodeHandle n_;
  ros::Publisher pose_pub_;

  public:
  void init()
  {
    //header - this is impt

    //Clear out our cmd - these values are roundabout initials
    cmd.linear.x=0.9;
    cmd.linear.y=0;
    cmd.linear.z=-0;
    cmd.angular.x=0;
    cmd.angular.y=0;
    cmd.angular.z=0.00145617884538;

    pose_pub_ = n_.advertise<geometry_msgs::Twist>("/cmd_vel", 1);

    ros::NodeHandle n_private("~");
  }

  ~TeleopPR2Keyboard()   { }
  void keyboardLoop();
};

int kfd = 0;
struct termios cooked, raw;

void quit(int sig)
{
  tcsetattr(kfd, TCSANOW, &cooked);
  exit(0);
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "pr2_arms_keyboard");

  TeleopPR2Keyboard tpk;
  tpk.init();

  signal(SIGINT,quit);

  tpk.keyboardLoop();

  return(0);
}

void TeleopPR2Keyboard::keyboardLoop()
{
  char c;
  bool dirty=false;

  // get the console in raw mode
  tcgetattr(kfd, &cooked);
  memcpy(&raw, &cooked, sizeof(struct termios));
  raw.c_lflag &=~ (ICANON | ECHO);
  // Setting a new line, then end of file
  raw.c_cc[VEOL] = 1;
  raw.c_cc[VEOF] = 2;
  tcsetattr(kfd, TCSANOW, &raw);

  puts("Reading from keyboard");
  puts("---------------------------");
  puts("Use 'WS' to forward/back");
  puts("Use 'AD' to left/right");
  puts("Use 'Q' to stop");

  for(;;)
  {
    // get the next event from the keyboard
    if(read(kfd, &c, 1) < 0)
    {
      perror("read():");
      exit(-1);
    }

    switch(c)
    {
      // Walking
    case KEYCODE_W:
      if(cmd.linear.x <2.5)
        cmd.linear.x = cmd.linear.x+0.25;
      dirty = true;
      break;
    case KEYCODE_S:
      if(cmd.linear.x >-2.5)
        cmd.linear.x = cmd.linear.x-0.25;
      dirty = true;
      break;
    case KEYCODE_A:
      if(cmd.angular.z<1.5)
        cmd.angular.z = cmd.angular.z+0.1;
      dirty = true;
      break;
    case KEYCODE_D:
      if(cmd.angular.z>-1.5)
        cmd.angular.z = cmd.angular.z-0.1;
      dirty = true;
      break;
    case KEYCODE_Q:
      cmd.angular.z = 0;
      cmd.linear.x = 0;
      dirty = true;
      break;  
    }


    if (dirty == true)
    {
      pose_pub_.publish(cmd);
    }


  }
}