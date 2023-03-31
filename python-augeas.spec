Name:		python-augeas
Version:	1.1.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/python-augeas/python-augeas-%{version}.tar.gz
Summary:	Python bindings for Augeas
URL:		https://pypi.org/project/parsedatetime/
License:	Apache License 2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	pkgconfig(augeas)
BuildRequires:	pkgconfig(python3)
BuildArch:	noarch
# The library is dlopen-ed -- no automated dependency generation
Requires:	%mklibname augeas

%description
Python bindings for Augeas

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/augeas
%{py_sitedir}/augeas.py
%{py_sitedir}/test
%{py_sitedir}/python_augeas-*.*-info
