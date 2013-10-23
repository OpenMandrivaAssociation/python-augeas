%define	release	%mkrel 1

Name:		python-augeas
Version:	0.4.1
Release:	1
Summary:	Python bindings to augeas
Group:		Development/Python
License:	LGPLv2+
Url:		http://augeas.net/
Source0:	http://augeas.net/download/python/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	libaugeas-devel
BuildRequires:	python-setuptools python-devel


%description
python-augeas is a set of Python bindings around augeas.

%prep
%setup -q


%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="%{optflags}" python setup.py build_ext -i
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install -O1 --skip-build --root=%{buildroot}

 
%clean

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README.txt
%{py_puresitedir}/augeas.py*
%{py_puresitedir}/*augeas*.egg-info


%changelog
* Tue Jan 25 2011 Guilherme Moro <guilherme@mandriva.com> 0.4.0-1mdv2011.0
+ Revision: 632650
- Initial import of the package
- Created package structure for python-augeas.


