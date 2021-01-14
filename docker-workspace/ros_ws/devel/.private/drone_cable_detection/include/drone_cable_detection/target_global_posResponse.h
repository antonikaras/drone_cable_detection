// Generated by gencpp from file drone_cable_detection/target_global_posResponse.msg
// DO NOT EDIT!


#ifndef DRONE_CABLE_DETECTION_MESSAGE_TARGET_GLOBAL_POSRESPONSE_H
#define DRONE_CABLE_DETECTION_MESSAGE_TARGET_GLOBAL_POSRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace drone_cable_detection
{
template <class ContainerAllocator>
struct target_global_posResponse_
{
  typedef target_global_posResponse_<ContainerAllocator> Type;

  target_global_posResponse_()
    : dist(0.0)  {
    }
  target_global_posResponse_(const ContainerAllocator& _alloc)
    : dist(0.0)  {
  (void)_alloc;
    }



   typedef double _dist_type;
  _dist_type dist;





  typedef boost::shared_ptr< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> const> ConstPtr;

}; // struct target_global_posResponse_

typedef ::drone_cable_detection::target_global_posResponse_<std::allocator<void> > target_global_posResponse;

typedef boost::shared_ptr< ::drone_cable_detection::target_global_posResponse > target_global_posResponsePtr;
typedef boost::shared_ptr< ::drone_cable_detection::target_global_posResponse const> target_global_posResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::drone_cable_detection::target_global_posResponse_<ContainerAllocator1> & lhs, const ::drone_cable_detection::target_global_posResponse_<ContainerAllocator2> & rhs)
{
  return lhs.dist == rhs.dist;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::drone_cable_detection::target_global_posResponse_<ContainerAllocator1> & lhs, const ::drone_cable_detection::target_global_posResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace drone_cable_detection

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3f4fece6412db25720b2bab9f80b3473";
  }

  static const char* value(const ::drone_cable_detection::target_global_posResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3f4fece6412db257ULL;
  static const uint64_t static_value2 = 0x20b2bab9f80b3473ULL;
};

template<class ContainerAllocator>
struct DataType< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "drone_cable_detection/target_global_posResponse";
  }

  static const char* value(const ::drone_cable_detection::target_global_posResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 dist\n"
;
  }

  static const char* value(const ::drone_cable_detection::target_global_posResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.dist);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct target_global_posResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::drone_cable_detection::target_global_posResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::drone_cable_detection::target_global_posResponse_<ContainerAllocator>& v)
  {
    s << indent << "dist: ";
    Printer<double>::stream(s, indent + "  ", v.dist);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DRONE_CABLE_DETECTION_MESSAGE_TARGET_GLOBAL_POSRESPONSE_H