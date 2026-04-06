Name:           zfsbootmenu
Version:        3.1.0
Release:        1%{?dist}
Summary:        Boot loader to boot from root file systems in zfs

License:        MIT
URL:            https://github.com/zbm-dev/zfsbootmenu
Source0:        https://github.com/zbm-dev/zfsbootmenu/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

Requires:       dracut kexec-tools zfs
Requires:       coreutils findutils binutils util-linux-core
Requires:       gawk perl
Requires:       bash glibc ncurses

BuildRequires: make

%description
ZFSBootMenu is a Linux bootloader that attempts to provide an experience
similar to FreeBSD's bootloader. By taking advantage of ZFS features,
it allows a user to have multiple "boot environments" (with different
distributions, for example), manipulate snapshots before booting, and, for
the adventurous user, even bootstrap a system installation via zfs recv.

If ZFSBootMenu is launched via EFI, then this package is probably not
needed to install. This package would be required for booting via BIOS.

%prep
%autosetup -n zfsbootmenu-%{version}

%build
# Nothing to do

%install
%make_install

# *** WARNING: ./usr/share/examples/zfsbootmenu/syslinux.cfg is executable but has no shebang, removing executable bit
# *** WARNING: ./usr/share/examples/zfsbootmenu/hooks/README.md is executable but has no shebang, removing executable bit
# *** WARNING: ./usr/share/examples/zfsbootmenu/refind_linux.conf is executable but has no shebang, removing executable bit
chmod -x \
        %{buildroot}/usr/share/examples/zfsbootmenu/syslinux.cfg \
        %{buildroot}/usr/share/examples/zfsbootmenu/hooks/README.md \
        %{buildroot}/usr/share/examples/zfsbootmenu/refind_linux.conf

find %{buildroot}/usr/share/zfsbootmenu %{buildroot}/usr/lib/dracut/modules.d -name '*.sh' -print0 | xargs -0 chmod +x

chmod +x %{buildroot}/usr/lib/initcpio/*/zfsbootmenu

%files
%license LICENSE
%doc README.md

%config(noreplace) /etc/zfsbootmenu/config.yaml
%config(noreplace) /etc/zfsbootmenu/dracut.conf.d/omit-drivers.conf
%config(noreplace) /etc/zfsbootmenu/dracut.conf.d/zfsbootmenu.conf
%config(noreplace) /etc/zfsbootmenu/mkinitcpio.conf
/usr/bin/*
%dir /usr/lib/dracut/modules.d/90zfsbootmenu
/usr/lib/dracut/modules.d/90zfsbootmenu/*
/usr/lib/initcpio/hooks/zfsbootmenu
/usr/lib/initcpio/install/zfsbootmenu
%dir /usr/share/examples/zfsbootmenu
/usr/share/examples/zfsbootmenu/*
/usr/share/man/man5/*
/usr/share/man/man7/*
/usr/share/man/man8/*
%dir /usr/share/zfsbootmenu
/usr/share/zfsbootmenu/*

%changelog
# LC_ALL=C date +'* %a %b %d %Y Håkon Løvdal <kode@denkule.no> - 3.1.x-1'
* Mon Apr 06 2026 Håkon Løvdal <kode@denkule.no> - 3.1.0-1
- Initial package
