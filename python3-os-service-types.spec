#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (incomplete dependencies)

Summary:	Python library for consuming OpenStack sevice-types-authority data
Summary(pl.UTF-8):	Biblioteka Pythona do konsumowania danych OpenStack sevice-types-authority
Name:		python3-os-service-types
Version:	1.8.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/os-service-types/
Source0:	https://files.pythonhosted.org/packages/source/o/os-service-types/os_service_types-%{version}.tar.gz
# Source0-md5:	b594a8f049246720eb1dd9910a740d5a
URL:		https://pypi.org/project/os-service-types/
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-pbr >= 6.1.1
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-keystoneauth1 >= 3.4.0
BuildRequires:	python3-oslotest >= 3.8.0
BuildRequires:	python3-requests-mock >= 1.2.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-testscenarios >= 0.4
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-openstackdocstheme >= 2.2.1
BuildRequires:	python3-reno >= 3.1.0
BuildRequires:	sphinx-pdg-3 >= 2.1.1
%endif
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python library for consuming OpenStack sevice-types-authority data.

The "OpenStack Service Types Authority" contains information about
official OpenStack services and their historical service-type aliases.

%description -l pl.UTF-8
Biblioteka Pythona do konsumowania danych OpenStack
sevice-types-authority.

Dane "OpenStack Service Types Authority" zawierają informacje o
oficjalnych usługach OpenStack i ich historycznych aliasach
service-type.

%package apidocs
Summary:	API documentation for Python os-service-types module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona os-service-types
Group:		Documentation

%description apidocs
API documentation for Python os-service-types module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona os-service-types.

%prep
%setup -q -n os_service_types-%{version}

%build
%py3_build

%if %{with tests}
stestr run
%endif

%if %{with doc}
sphinx-build-3 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/os_service_types/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/os_service_types
%{py3_sitescriptdir}/os_service_types-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,library,reference,*.html,*.js}
%endif
