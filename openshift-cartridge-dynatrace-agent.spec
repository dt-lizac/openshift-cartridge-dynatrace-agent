%global cartridgedir %{_libexecdir}/openshift/cartridges/dynatrace-agent-6
Name:		openshift-cartridge-dynatrace-agent
Version:	0.0.12
Release:	1%{?dist}
Summary:	Dynatrace Monitoring for Java applications deployed on OpenShift JBoss cartridges
Group:		Applications/Internet
License:	ASL 2.0
URL:		http://www.dynatrace.com
#Source0:	https://github.com/akirasoft/openshift-cartridge-dynatrace-agent/archive/master.zip
Source0:        %{name}-%{version}.tar.gz
Requires:       rubygem(openshift-origin-node)
Requires:       openshift-origin-node-util
BuildArch:      x86_64
%define _unpackaged_files_terminate_build 0
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Dynatrace Monitoring for Java applications deployed on OpenShift JBoss cartridges

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{cartridgedir}
cp -r * %{buildroot}%{cartridgedir}/

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/conf/
%{cartridgedir}/env
%dir %{cartridgedir}/metadata
%{cartridgedir}/versions
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/LICENSE

%changelog
