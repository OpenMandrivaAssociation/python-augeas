%define	release	%mkrel 1

Name:		python-augeas
Version:	0.4.0
Release:	%release
Summary:	Python bindings to augeas
Group:		Development/Python
License:	LGPLv2+
Url:		http://augeas.net/
Source0:	http://augeas.net/download/python/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	libaugeas-devel
BuildRequires:	python-setuptools python-devel


%description
python-augeas is a set of Python bindings around augeas.

%prep
%setup -q


%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" python setup.py build_ext -i
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README.txt
%{py_sitedir}/augeas.py*
%{py_sitedir}/*augeas*.egg-info
