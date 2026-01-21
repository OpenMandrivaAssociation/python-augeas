Name:		python-augeas
Version:	1.2.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/python-augeas/python-augeas-%{version}.tar.gz
Summary:	Python bindings for Augeas
URL:		https://pypi.org/project/python-augeas/
License:	Apache License 2.0
Group:		Development/Python
BuildSystem:	python
BuildRequires:	pkgconfig(augeas)
BuildRequires:	pkgconfig(python3)

%description
Python bindings for Augeas

%files
%{py_platsitedir}/_augeas.abi*.so
%{py_platsitedir}/augeas
%{py_platsitedir}/python_augeas-*.*-info
