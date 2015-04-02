Name:           ros-hydro-bwi-desktop-full
Version:        0.3.1
Release:        1%{?dist}
Summary:        ROS bwi_desktop_full package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/bwi_desktop_full
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-bloom
Requires:       python-catkin_tools
Requires:       python-rosinstall
Requires:       python-wstool
Requires:       ros-hydro-bwi-desktop
BuildRequires:  ros-hydro-catkin

%description
ROS desktop full metapackage for the Building-Wide Intelligence (BWI) project of
the University of Texas at Austin. It depends on all released BWI packages and
some other useful ROS packages. These packages include GUI components.

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

