Name:       sailfish-browser-disablewordsnapselection-patch

# >> macros
BuildArch: noarch
# << macros

Summary:    Disable word snap selection in Browser
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   sailfish-browser-textselection-patch
Requires:   sailfish-browser >= 1.1.3.2

%description
A sailfish-browser patch disabling snap to word when selection text


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfish-browser-disablewordsnapselection-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfish-browser-disablewordsnapselection-patch
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfish-browser-disablewordsnapselection-patch
# >> files
# << files
