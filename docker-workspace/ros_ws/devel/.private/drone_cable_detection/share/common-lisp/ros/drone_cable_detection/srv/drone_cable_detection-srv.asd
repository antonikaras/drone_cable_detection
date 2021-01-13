
(cl:in-package :asdf)

(defsystem "drone_cable_detection-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :mavros_msgs-msg
)
  :components ((:file "_package")
    (:file "align_with_wire" :depends-on ("_package_align_with_wire"))
    (:file "_package_align_with_wire" :depends-on ("_package"))
    (:file "target_global_pos" :depends-on ("_package_target_global_pos"))
    (:file "_package_target_global_pos" :depends-on ("_package"))
    (:file "target_local_pos" :depends-on ("_package_target_local_pos"))
    (:file "_package_target_local_pos" :depends-on ("_package"))
  ))