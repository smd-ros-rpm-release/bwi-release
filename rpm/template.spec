Name:           ros-hydro-bwi-launch
Version:        0.3.1
Release:        1%{?dist}
Summary:        ROS bwi_launch package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-bwi-kr-execution
Requires:       ros-hydro-multi-level-map-server
Requires:       ros-hydro-multi-level-map-utils
Requires:       ros-hydro-segbot-bringup
Requires:       ros-hydro-segbot-gazebo
Requires:       ros-hydro-segbot-gui
Requires:       ros-hydro-segbot-logical-translator
Requires:       ros-hydro-segbot-navigation
Requires:       ros-hydro-segbot-simulation-apps
Requires:       ros-hydro-utexas-gdc
BuildRequires:  ros-hydro-bwi-kr-execution
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-multi-level-map-server
BuildRequires:  ros-hydro-multi-level-map-utils
BuildRequires:  ros-hydro-roslaunch
BuildRequires:  ros-hydro-segbot-bringup
BuildRequires:  ros-hydro-segbot-gazebo
BuildRequires:  ros-hydro-segbot-gui
BuildRequires:  ros-hydro-segbot-logical-translator
BuildRequires:  ros-hydro-segbot-navigation
BuildRequires:  ros-hydro-segbot-simulation-apps
BuildRequires:  ros-hydro-utexas-gdc

%description
Top-level ROS launch scripts for the Building-Wide Intelligence (BWI) project of
the University of Texas at Austin.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Apr 01 2015 Jack O'Quin <jack.oquin@gmail.com> - 0.3.1-1
- Autogenerated by Bloom

