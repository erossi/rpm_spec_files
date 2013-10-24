%define python_version python2.7

Name: python-whoosh
Version: 2.3.2
Release: jrc.1
Url: http://bitbucket.org/mchaput/whoosh/
Summary: pure-Python full-text indexing, search, and spell checking library
License: GPL
Group: Development/Languages/Python
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build
BuildArch: noarch
Vendor: Daniel Watkins <daniel.watkins@credativ.co.uk>
Packager: Enrico Rossi <enrico.rossi@jrc.ec.europa.eu>
# BuildRequires: python2.6
Requires: python27

%define wh_prefix %{_datadir}/%{name}

%description
 Whoosh is a fast, pure-Python indexing and search library. Programmers
 can use it to easily add search functionality to their applications and
 websites. As Whoosh is pure Python, you don't have to compile or
 install a binary support library and/or make Python work with a JVM, yet
 indexing and searching is still very fast. Whoosh is designed to be
 modular, so every part can be extended or replaced to meet your needs
 exactly.

%prep
#%setup -n %{name}-%{unmangled_version}
%setup -n Whoosh-2.3.2

%build
%{python_version} setup.py build

%install
%{python_version} setup.py install --prefix=%{_prefix} --root=%{buildroot} --no-compile

#python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT \
#	--record=INSTALLED_FILES \
#	--install-lib=%{wh_prefix} \
#	--install-scripts=%{wh_prefix} \
#	--prefix=%{wh_prefix}

# Better to add a patch not to install these files in the
# 1st place.
#rm %{buildroot}/%{cbrn_prefix}/python-modules/*.py[co]
#rm %{buildroot}/%{cbrn_prefix}/*.egg-info
rm -r %{buildroot}/usr/lib/python2.7/site-packages/W*

%clean
rm -rf $RPM_BUILD_ROOT

# Specify all the files and directories by hand.
# %files -f INSTALLED_FILES
%files
%defattr(-,root,root)
/usr/lib/python2.7/site-packages/whoosh/

%changelog
* Fri Aug 30 2013 Enrico Rossi <enrico.rossi@ext.ec.europa.eu> 2.0-jrc.1
- Start RPM packaging.
