Name:           ros-kinetic-openni-camera
Version:        1.9.5
Release:        0%{?dist}
Summary:        ROS openni_camera package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/openni_camera
Source0:        %{name}-%{version}.tar.gz

Requires:       libusbx-devel
Requires:       log4cxx-devel
Requires:       openni-devel
Requires:       ros-kinetic-camera-info-manager
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  libusbx-devel
BuildRequires:  log4cxx-devel
BuildRequires:  openni-devel
BuildRequires:  ros-kinetic-camera-info-manager
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs

%description
A ROS driver for OpenNI depth (+ RGB) cameras. These include: Microsoft Kinect,
PrimeSense PSDK, ASUS Xtion Pro and Pro Live The driver publishes raw depth,
RGB, and IR image streams.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Apr 03 2016 Isaac I.Y. Saito <130s@2000.jukuin.keio.ac.jp> - 1.9.5-0
- Autogenerated by Bloom

