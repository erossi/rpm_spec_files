#
# spec file for package python-bottle
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define python_version python2.7

Name:           python27-bottle
Version:        0.10.11
Release:        jrc.1
Url:            http://bottlepy.org/
Summary:        Fast and simple WSGI-framework for small web-applications
License:        MIT
Group:          Development/Languages/Python
Source:         bottle-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Packager:       Enrico Rossi <enrico.rossi@ext.ec.europa.eu>

%description
Bottle is a fast and simple micro-framework for small web-applications. It offers request dispatching (Routes) with url parameter support, Templates, a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and template engines. All in a single file and with no dependencies other than the Python Standard Library.

%prep
%setup -q -n bottle-%{version}

%build
%{python_version} setup.py build

%install
%{python_version} setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm %{buildroot}/usr/lib/%{python_version}/site-packages/*.egg-info
# rm %{buildroot}/usr/lib/%{python_version}/site-packages/*.py[co]
rm %{buildroot}%{_bindir}/bottle.py

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.rst
/usr/lib/%{python_version}/site-packages/bottle.*

%changelog
* Mon Sep  2 2013 enrico.rossi@ext.ec.europa.eu
- Merging Debian package and Opensuse SRPM to version 0.10.11.
- Initial build
