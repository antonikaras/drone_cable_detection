; Auto-generated. Do not edit!


(cl:in-package drone_cable_detection-srv)


;//! \htmlinclude align_with_wire-request.msg.html

(cl:defclass <align_with_wire-request> (roslisp-msg-protocol:ros-message)
  ((timeOut
    :reader timeOut
    :initarg :timeOut
    :type cl:float
    :initform 0.0))
)

(cl:defclass align_with_wire-request (<align_with_wire-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <align_with_wire-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'align_with_wire-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_cable_detection-srv:<align_with_wire-request> is deprecated: use drone_cable_detection-srv:align_with_wire-request instead.")))

(cl:ensure-generic-function 'timeOut-val :lambda-list '(m))
(cl:defmethod timeOut-val ((m <align_with_wire-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_cable_detection-srv:timeOut-val is deprecated.  Use drone_cable_detection-srv:timeOut instead.")
  (timeOut m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <align_with_wire-request>) ostream)
  "Serializes a message object of type '<align_with_wire-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'timeOut))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <align_with_wire-request>) istream)
  "Deserializes a message object of type '<align_with_wire-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'timeOut) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<align_with_wire-request>)))
  "Returns string type for a service object of type '<align_with_wire-request>"
  "drone_cable_detection/align_with_wireRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'align_with_wire-request)))
  "Returns string type for a service object of type 'align_with_wire-request"
  "drone_cable_detection/align_with_wireRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<align_with_wire-request>)))
  "Returns md5sum for a message object of type '<align_with_wire-request>"
  "cbc1dbe05903c9604fb7ff840d1f16c4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'align_with_wire-request)))
  "Returns md5sum for a message object of type 'align_with_wire-request"
  "cbc1dbe05903c9604fb7ff840d1f16c4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<align_with_wire-request>)))
  "Returns full string definition for message of type '<align_with_wire-request>"
  (cl:format cl:nil "float64 timeOut~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'align_with_wire-request)))
  "Returns full string definition for message of type 'align_with_wire-request"
  (cl:format cl:nil "float64 timeOut~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <align_with_wire-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <align_with_wire-request>))
  "Converts a ROS message object to a list"
  (cl:list 'align_with_wire-request
    (cl:cons ':timeOut (timeOut msg))
))
;//! \htmlinclude align_with_wire-response.msg.html

(cl:defclass <align_with_wire-response> (roslisp-msg-protocol:ros-message)
  ((wire_pos
    :reader wire_pos
    :initarg :wire_pos
    :type mavros_msgs-msg:PositionTarget
    :initform (cl:make-instance 'mavros_msgs-msg:PositionTarget)))
)

(cl:defclass align_with_wire-response (<align_with_wire-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <align_with_wire-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'align_with_wire-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_cable_detection-srv:<align_with_wire-response> is deprecated: use drone_cable_detection-srv:align_with_wire-response instead.")))

(cl:ensure-generic-function 'wire_pos-val :lambda-list '(m))
(cl:defmethod wire_pos-val ((m <align_with_wire-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_cable_detection-srv:wire_pos-val is deprecated.  Use drone_cable_detection-srv:wire_pos instead.")
  (wire_pos m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <align_with_wire-response>) ostream)
  "Serializes a message object of type '<align_with_wire-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'wire_pos) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <align_with_wire-response>) istream)
  "Deserializes a message object of type '<align_with_wire-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'wire_pos) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<align_with_wire-response>)))
  "Returns string type for a service object of type '<align_with_wire-response>"
  "drone_cable_detection/align_with_wireResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'align_with_wire-response)))
  "Returns string type for a service object of type 'align_with_wire-response"
  "drone_cable_detection/align_with_wireResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<align_with_wire-response>)))
  "Returns md5sum for a message object of type '<align_with_wire-response>"
  "cbc1dbe05903c9604fb7ff840d1f16c4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'align_with_wire-response)))
  "Returns md5sum for a message object of type 'align_with_wire-response"
  "cbc1dbe05903c9604fb7ff840d1f16c4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<align_with_wire-response>)))
  "Returns full string definition for message of type '<align_with_wire-response>"
  (cl:format cl:nil "mavros_msgs/PositionTarget wire_pos~%~%~%================================================================================~%MSG: mavros_msgs/PositionTarget~%# Message for SET_POSITION_TARGET_LOCAL_NED~%#~%# Some complex system requires all feautures that mavlink~%# message provide. See issue #402.~%~%std_msgs/Header header~%~%uint8 coordinate_frame~%uint8 FRAME_LOCAL_NED = 1~%uint8 FRAME_LOCAL_OFFSET_NED = 7~%uint8 FRAME_BODY_NED = 8~%uint8 FRAME_BODY_OFFSET_NED = 9~%~%uint16 type_mask~%uint16 IGNORE_PX = 1	# Position ignore flags~%uint16 IGNORE_PY = 2~%uint16 IGNORE_PZ = 4~%uint16 IGNORE_VX = 8	# Velocity vector ignore flags~%uint16 IGNORE_VY = 16~%uint16 IGNORE_VZ = 32~%uint16 IGNORE_AFX = 64	# Acceleration/Force vector ignore flags~%uint16 IGNORE_AFY = 128~%uint16 IGNORE_AFZ = 256~%uint16 FORCE = 512	# Force in af vector flag~%uint16 IGNORE_YAW = 1024~%uint16 IGNORE_YAW_RATE = 2048~%~%geometry_msgs/Point position~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 acceleration_or_force~%float32 yaw~%float32 yaw_rate~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'align_with_wire-response)))
  "Returns full string definition for message of type 'align_with_wire-response"
  (cl:format cl:nil "mavros_msgs/PositionTarget wire_pos~%~%~%================================================================================~%MSG: mavros_msgs/PositionTarget~%# Message for SET_POSITION_TARGET_LOCAL_NED~%#~%# Some complex system requires all feautures that mavlink~%# message provide. See issue #402.~%~%std_msgs/Header header~%~%uint8 coordinate_frame~%uint8 FRAME_LOCAL_NED = 1~%uint8 FRAME_LOCAL_OFFSET_NED = 7~%uint8 FRAME_BODY_NED = 8~%uint8 FRAME_BODY_OFFSET_NED = 9~%~%uint16 type_mask~%uint16 IGNORE_PX = 1	# Position ignore flags~%uint16 IGNORE_PY = 2~%uint16 IGNORE_PZ = 4~%uint16 IGNORE_VX = 8	# Velocity vector ignore flags~%uint16 IGNORE_VY = 16~%uint16 IGNORE_VZ = 32~%uint16 IGNORE_AFX = 64	# Acceleration/Force vector ignore flags~%uint16 IGNORE_AFY = 128~%uint16 IGNORE_AFZ = 256~%uint16 FORCE = 512	# Force in af vector flag~%uint16 IGNORE_YAW = 1024~%uint16 IGNORE_YAW_RATE = 2048~%~%geometry_msgs/Point position~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 acceleration_or_force~%float32 yaw~%float32 yaw_rate~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <align_with_wire-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'wire_pos))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <align_with_wire-response>))
  "Converts a ROS message object to a list"
  (cl:list 'align_with_wire-response
    (cl:cons ':wire_pos (wire_pos msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'align_with_wire)))
  'align_with_wire-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'align_with_wire)))
  'align_with_wire-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'align_with_wire)))
  "Returns string type for a service object of type '<align_with_wire>"
  "drone_cable_detection/align_with_wire")