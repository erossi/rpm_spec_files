Name:           libjs-jquery
URL:            http://jquery.com/
Summary:        Fast and concise JavaScript Library
Version:        1.9.1
Release:        jrc.1
License:        MIT or GPLv2+
Group:          Productivity/Networking/Web/Utilities
Source:	        http://code.jquery.com/jquery-%{version}.min.js
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Packager:       Enrico Rossi <enrico.rossi@ext.ec.europa.eu>

%define jsname jquery
%define js_v_name %{jsname}-%{version}
%define jsdir /usr/share/javascript/%{jsname}

%description 
jQuery is a fast and concise JavaScript Library that simplifies HTML
document traversing, event handling, animating, and Ajax
interactions for rapid web development. jQuery is designed to change
the way that you write JavaScript.

%prep
%setup -Tc

%build

%install
install -d --mode=755 %{buildroot}%{jsdir}
install --mode=644 %{_sourcedir}/%{js_v_name}.min.js %{buildroot}%{jsdir}

# link version-less js
ln -s %{js_v_name}.min.js %{buildroot}%{jsdir}/%{jsname}.js
ln -s %{js_v_name}.min.js %{buildroot}%{jsdir}/%{jsname}.min.js

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{jsdir}
