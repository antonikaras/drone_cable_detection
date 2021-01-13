// Auto-generated. Do not edit!

// (in-package drone_cable_detection.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

let mavros_msgs = _finder('mavros_msgs');

//-----------------------------------------------------------

class align_with_wireRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.timeOut = null;
    }
    else {
      if (initObj.hasOwnProperty('timeOut')) {
        this.timeOut = initObj.timeOut
      }
      else {
        this.timeOut = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type align_with_wireRequest
    // Serialize message field [timeOut]
    bufferOffset = _serializer.float64(obj.timeOut, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type align_with_wireRequest
    let len;
    let data = new align_with_wireRequest(null);
    // Deserialize message field [timeOut]
    data.timeOut = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'drone_cable_detection/align_with_wireRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a7a138008fb2d0c41d90d6ef0f7caaf3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 timeOut
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new align_with_wireRequest(null);
    if (msg.timeOut !== undefined) {
      resolved.timeOut = msg.timeOut;
    }
    else {
      resolved.timeOut = 0.0
    }

    return resolved;
    }
};

class align_with_wireResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.wire_pos = null;
    }
    else {
      if (initObj.hasOwnProperty('wire_pos')) {
        this.wire_pos = initObj.wire_pos
      }
      else {
        this.wire_pos = new mavros_msgs.msg.PositionTarget();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type align_with_wireResponse
    // Serialize message field [wire_pos]
    bufferOffset = mavros_msgs.msg.PositionTarget.serialize(obj.wire_pos, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type align_with_wireResponse
    let len;
    let data = new align_with_wireResponse(null);
    // Deserialize message field [wire_pos]
    data.wire_pos = mavros_msgs.msg.PositionTarget.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += mavros_msgs.msg.PositionTarget.getMessageSize(object.wire_pos);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'drone_cable_detection/align_with_wireResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '70b7e82d61118589c50617280ce32f1e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    float64 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new align_with_wireResponse(null);
    if (msg.wire_pos !== undefined) {
      resolved.wire_pos = mavros_msgs.msg.PositionTarget.Resolve(msg.wire_pos)
    }
    else {
      resolved.wire_pos = new mavros_msgs.msg.PositionTarget()
    }

    return resolved;
    }
};

module.exports = {
  Request: align_with_wireRequest,
  Response: align_with_wireResponse,
  md5sum() { return 'cbc1dbe05903c9604fb7ff840d1f16c4'; },
  datatype() { return 'drone_cable_detection/align_with_wire'; }
};
