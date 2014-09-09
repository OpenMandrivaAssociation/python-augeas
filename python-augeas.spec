Name:		python-augeas
Version:	0.5.0
Release:	1
Summary:	Python bindings to augeas
Group:		Development/Python
License:	LGPLv2+
Url:		http://augeas.net/
Source0:	https://fedorahosted.org/released/python-augeas/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	pkgconfig(augeas)
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
%doc COPYING AUTHORS README.txt
%{py_puresitedir}/augeas.py*
%{py_puresitedir}/*augeas*.egg-info
