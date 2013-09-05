Name:           libjs-jquery-ui
URL:            http://jqueryui.com/
Summary:        JavaScript UI library for dynamic web applications
Version:        1.9.2
Release:        jrc.1
License:        MIT
Group:          Productivity/Networking/Web/Utilities
Source:	        jquery-ui-1.9.2.custom.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:	libjs-jquery
Packager:       Enrico Rossi <enrico.rossi@ext.ec.europa.eu>

%define jsname jquery-ui
%define js_v_name %{jsname}-%{version}
%define js_vc_name %{jsname}-%{version}.custom
%define jsdir /usr/share/javascript/%{jsname}
%define docdir /usr/share/doc/%{name}

%description 
JavaScript UI library for dynamic web applications jQuery UI provides
abstractions for low-level interaction and animation, advanced effects
and high-level, themeable widgets, built on top of the jQuery JavaScript
Library, that you can use to build highly interactive web applications.

This version contains the basic and smoothness themes.

%prep
%setup -q -n jquery-ui-1.9.2.custom

%build

%install
install -d --mode=755 %{buildroot}%{jsdir}
cp -a css %{buildroot}%{jsdir}
cp -a development-bundle/themes %{buildroot}%{jsdir}
cp -a development-bundle/ui %{buildroot}%{jsdir}
install --mode=644 js/%{js_vc_name}.js %{buildroot}%{jsdir}/ui
install --mode=644 js/%{js_vc_name}.min.js %{buildroot}%{jsdir}/ui

install -d --mode=755 %{buildroot}%{docdir}
install --mode=644 development-bundle/AUTHORS.txt %{buildroot}%{docdir}
install --mode=644 development-bundle/MIT-LICENSE.txt %{buildroot}%{docdir}

# link version-less css
ln -s %{js_vc_name}.css %{buildroot}%{jsdir}/css/smoothness/%{jsname}.css
ln -s %{js_vc_name}.min.css %{buildroot}%{jsdir}/css/smoothness/%{jsname}.min.css
# link version-less js
ln -s ui/%{js_vc_name}.js %{buildroot}%{jsdir}/%{jsname}.js
ln -s ui/%{js_vc_name}.min.js %{buildroot}%{jsdir}/%{jsname}.min.js

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%dir %{jsdir}
%dir %{docdir}
%{jsdir}
%{docdir}
