Name: Crystal_splice
# version is also in makefile and Version.txt
Version: 1.3.0
License: C4X
%{!?buildnumber:%define buildnumber 1}
Release: %{?buildnumber}%{?dist}
BuildArch: noarch
Group: Productivity/Scientific/Chemistry
Summary: This is the Crystal splice script, which allows for modes to be inserted into base of different torsion
Requires: python bash 
BuildRequires: make bash
URL: http://dna.conformetrix.com/helpconsole6/Software%20Manuals/default.aspx#pageid=%{name}
Source: %{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is the Crystal splice script, which allows for modes to be inserted into
base of different torsion

%prep
%setup -q

%build
make -f makefile %{?_smp_mflags} NAME=%{name} VERSION=%{version} build

%check
make -f makefile NAME=%{name} VERSION=%{version} check

%install
/usr/bin/mkdir -p "%{buildroot}%{_bindir}" 
/usr/bin/install -D "crystalsplice" "%{buildroot}%{_bindir}/"
/usr/bin/mkdir -p "%{buildroot}%{_datadir}/%{name}" 
/usr/bin/cp     scr/*.py "%{buildroot}%{_datadir}/%{name}/"

%pre

%preun
	
%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &>/dev/null || :
update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
# really uninstalling
	touch --no-create %{_datadir}/icons/hicolor &>/dev/null
	gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
	update-desktop-database &>/dev/null || :
	update-mime-database %{_datadir}/mime &>/dev/null || :
fi

%files
%defattr(644,root,root,-)
%{_datadir}/%{name}
%defattr(755,root,root,-)
%{_bindir}/*


%changelog
* Mon Mar 13 2017 Mike Denison <michael.denison@c4xdiscovery.com> 1.3.0-1
Trying remove multiple version
* Mon Mar 13 2017 Mike Denison <michael.denison@c4xdiscovery.com> 1.1.0-1
This is an updated version, due to C4X_11188 which used conf, a current patch has been added, 
where the config is now added, but does not have a crystal mode
* Mon Mar 13 2017 Mike Denison <michael.denison@c4xdiscovery.com> 1.0.0-1
This is a working script, which is now for wider testing
