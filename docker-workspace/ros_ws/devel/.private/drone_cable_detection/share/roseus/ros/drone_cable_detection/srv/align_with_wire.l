;; Auto-generated. Do not edit!


(when (boundp 'drone_cable_detection::align_with_wire)
  (if (not (find-package "DRONE_CABLE_DETECTION"))
    (make-package "DRONE_CABLE_DETECTION"))
  (shadow 'align_with_wire (find-package "DRONE_CABLE_DETECTION")))
(unless (find-package "DRONE_CABLE_DETECTION::ALIGN_WITH_WIRE")
  (make-package "DRONE_CABLE_DETECTION::ALIGN_WITH_WIRE"))
(unless (find-package "DRONE_CABLE_DETECTION::ALIGN_WITH_WIREREQUEST")
  (make-package "DRONE_CABLE_DETECTION::ALIGN_WITH_WIREREQUEST"))
(unless (find-package "DRONE_CABLE_DETECTION::ALIGN_WITH_WIRERESPONSE")
  (make-package "DRONE_CABLE_DETECTION::ALIGN_WITH_WIRERESPONSE"))

(in-package "ROS")



(if (not (find-package "MAVROS_MSGS"))
  (ros::roseus-add-msgs "mavros_msgs"))


(defclass drone_cable_detection::align_with_wireRequest
  :super ros::object
  :slots (_timeOut ))

(defmethod drone_cable_detection::align_with_wireRequest
  (:init
   (&key
    ((:timeOut __timeOut) 0.0)
    )
   (send-super :init)
   (setq _timeOut (float __timeOut))
   self)
  (:timeOut
   (&optional __timeOut)
   (if __timeOut (setq _timeOut __timeOut)) _timeOut)
  (:serialization-length
   ()
   (+
    ;; float64 _timeOut
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _timeOut
       (sys::poke _timeOut (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _timeOut
     (setq _timeOut (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass drone_cable_detection::align_with_wireResponse
  :super ros::object
  :slots (_wire_pos ))

(defmethod drone_cable_detection::align_with_wireResponse
  (:init
   (&key
    ((:wire_pos __wire_pos) (instance mavros_msgs::PositionTarget :init))
    )
   (send-super :init)
   (setq _wire_pos __wire_pos)
   self)
  (:wire_pos
   (&rest __wire_pos)
   (if (keywordp (car __wire_pos))
       (send* _wire_pos __wire_pos)
     (progn
       (if __wire_pos (setq _wire_pos (car __wire_pos)))
       _wire_pos)))
  (:serialization-length
   ()
   (+
    ;; mavros_msgs/PositionTarget _wire_pos
    (send _wire_pos :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; mavros_msgs/PositionTarget _wire_pos
       (send _wire_pos :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; mavros_msgs/PositionTarget _wire_pos
     (send _wire_pos :deserialize buf ptr-) (incf ptr- (send _wire_pos :serialization-length))
   ;;
   self)
  )

(defclass drone_cable_detection::align_with_wire
  :super ros::object
  :slots ())

(setf (get drone_cable_detection::align_with_wire :md5sum-) "cbc1dbe05903c9604fb7ff840d1f16c4")
(setf (get drone_cable_detection::align_with_wire :datatype-) "drone_cable_detection/align_with_wire")
(setf (get drone_cable_detection::align_with_wire :request) drone_cable_detection::align_with_wireRequest)
(setf (get drone_cable_detection::align_with_wire :response) drone_cable_detection::align_with_wireResponse)

(defmethod drone_cable_detection::align_with_wireRequest
  (:response () (instance drone_cable_detection::align_with_wireResponse :init)))

(setf (get drone_cable_detection::align_with_wireRequest :md5sum-) "cbc1dbe05903c9604fb7ff840d1f16c4")
(setf (get drone_cable_detection::align_with_wireRequest :datatype-) "drone_cable_detection/align_with_wireRequest")
(setf (get drone_cable_detection::align_with_wireRequest :definition-)
      "float64 timeOut
---
mavros_msgs/PositionTarget wire_pos


================================================================================
MSG: mavros_msgs/PositionTarget
# Message for SET_POSITION_TARGET_LOCAL_NED
#
# Some complex system requires all feautures that mavlink
# message provide. See issue #402.

std_msgs/Header header

uint8 coordinate_frame
uint8 FRAME_LOCAL_NED = 1
uint8 FRAME_LOCAL_OFFSET_NED = 7
uint8 FRAME_BODY_NED = 8
uint8 FRAME_BODY_OFFSET_NED = 9

uint16 type_mask
uint16 IGNORE_PX = 1	# Position ignore flags
uint16 IGNORE_PY = 2
uint16 IGNORE_PZ = 4
uint16 IGNORE_VX = 8	# Velocity vector ignore flags
uint16 IGNORE_VY = 16
uint16 IGNORE_VZ = 32
uint16 IGNORE_AFX = 64	# Acceleration/Force vector ignore flags
uint16 IGNORE_AFY = 128
uint16 IGNORE_AFZ = 256
uint16 FORCE = 512	# Force in af vector flag
uint16 IGNORE_YAW = 1024
uint16 IGNORE_YAW_RATE = 2048

geometry_msgs/Point position
geometry_msgs/Vector3 velocity
geometry_msgs/Vector3 acceleration_or_force
float32 yaw
float32 yaw_rate

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
")

(setf (get drone_cable_detection::align_with_wireResponse :md5sum-) "cbc1dbe05903c9604fb7ff840d1f16c4")
(setf (get drone_cable_detection::align_with_wireResponse :datatype-) "drone_cable_detection/align_with_wireResponse")
(setf (get drone_cable_detection::align_with_wireResponse :definition-)
      "float64 timeOut
---
mavros_msgs/PositionTarget wire_pos


================================================================================
MSG: mavros_msgs/PositionTarget
# Message for SET_POSITION_TARGET_LOCAL_NED
#
# Some complex system requires all feautures that mavlink
# message provide. See issue #402.

std_msgs/Header header

uint8 coordinate_frame
uint8 FRAME_LOCAL_NED = 1
uint8 FRAME_LOCAL_OFFSET_NED = 7
uint8 FRAME_BODY_NED = 8
uint8 FRAME_BODY_OFFSET_NED = 9

uint16 type_mask
uint16 IGNORE_PX = 1	# Position ignore flags
uint16 IGNORE_PY = 2
uint16 IGNORE_PZ = 4
uint16 IGNORE_VX = 8	# Velocity vector ignore flags
uint16 IGNORE_VY = 16
uint16 IGNORE_VZ = 32
uint16 IGNORE_AFX = 64	# Acceleration/Force vector ignore flags
uint16 IGNORE_AFY = 128
uint16 IGNORE_AFZ = 256
uint16 FORCE = 512	# Force in af vector flag
uint16 IGNORE_YAW = 1024
uint16 IGNORE_YAW_RATE = 2048

geometry_msgs/Point position
geometry_msgs/Vector3 velocity
geometry_msgs/Vector3 acceleration_or_force
float32 yaw
float32 yaw_rate

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
")



(provide :drone_cable_detection/align_with_wire "cbc1dbe05903c9604fb7ff840d1f16c4")


