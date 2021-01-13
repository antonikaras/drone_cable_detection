// Generated by gencpp from file uav_mavros_simulation/goto_aruco.msg
// DO NOT EDIT!


#ifndef UAV_MAVROS_SIMULATION_MESSAGE_GOTO_ARUCO_H
#define UAV_MAVROS_SIMULATION_MESSAGE_GOTO_ARUCO_H

#include <ros/service_traits.h>


#include <uav_mavros_simulation/goto_arucoRequest.h>
#include <uav_mavros_simulation/goto_arucoResponse.h>


namespace uav_mavros_simulation
{

struct goto_aruco
{

typedef goto_arucoRequest Request;
typedef goto_arucoResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct goto_aruco
} // namespace uav_mavros_simulation


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::uav_mavros_simulation::goto_aruco > {
  static const char* value()
  {
    return "02fd582894f05f0c4b5cc3fc3ea23d3d";
  }

  static const char* value(const ::uav_mavros_simulation::goto_aruco&) { return value(); }
};

template<>
struct DataType< ::uav_mavros_simulation::goto_aruco > {
  static const char* value()
  {
    return "uav_mavros_simulation/goto_aruco";
  }

  static const char* value(const ::uav_mavros_simulation::goto_aruco&) { return value(); }
};


// service_traits::MD5Sum< ::uav_mavros_simulation::goto_arucoRequest> should match
// service_traits::MD5Sum< ::uav_mavros_simulation::goto_aruco >
template<>
struct MD5Sum< ::uav_mavros_simulation::goto_arucoRequest>
{
  static const char* value()
  {
    return MD5Sum< ::uav_mavros_simulation::goto_aruco >::value();
  }
  static const char* value(const ::uav_mavros_simulation::goto_arucoRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::uav_mavros_simulation::goto_arucoRequest> should match
// service_traits::DataType< ::uav_mavros_simulation::goto_aruco >
template<>
struct DataType< ::uav_mavros_simulation::goto_arucoRequest>
{
  static const char* value()
  {
    return DataType< ::uav_mavros_simulation::goto_aruco >::value();
  }
  static const char* value(const ::uav_mavros_simulation::goto_arucoRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::uav_mavros_simulation::goto_arucoResponse> should match
// service_traits::MD5Sum< ::uav_mavros_simulation::goto_aruco >
template<>
struct MD5Sum< ::uav_mavros_simulation::goto_arucoResponse>
{
  static const char* value()
  {
    return MD5Sum< ::uav_mavros_simulation::goto_aruco >::value();
  }
  static const char* value(const ::uav_mavros_simulation::goto_arucoResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::uav_mavros_simulation::goto_arucoResponse> should match
// service_traits::DataType< ::uav_mavros_simulation::goto_aruco >
template<>
struct DataType< ::uav_mavros_simulation::goto_arucoResponse>
{
  static const char* value()
  {
    return DataType< ::uav_mavros_simulation::goto_aruco >::value();
  }
  static const char* value(const ::uav_mavros_simulation::goto_arucoResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // UAV_MAVROS_SIMULATION_MESSAGE_GOTO_ARUCO_H
