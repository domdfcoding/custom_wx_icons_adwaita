#!/usr/bin/python3
#
#  __init__.py
#
#  Copyright (C) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Includes icons from the Adwaita Icon Theme
#  https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/adwaita-icon-theme/3.28.0-1ubuntu1/adwaita-icon-theme_3.28.0.orig.tar.xz
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# stdlib
from typing import Any, Optional, Tuple, Union

# 3rd party
import importlib_resources
import wx  # type: ignore
from wx_icons_hicolor import HicolorIconTheme, wxHicolorIconTheme
from wx_icons_hicolor.icon import Icon
from wx_icons_hicolor.icon_theme import IconTheme

# this package
from wx_icons_adwaita import Adwaita

__all__ = ["AdwaitaIconTheme", "version", "wxAdwaitaIconTheme"]

__version__: str = "0.1.2"


def version() -> str:
	return f"""wx_icons_adwaita
Version {__version__}
Adwaita Icon Theme Version 3.28.0
"""


with importlib_resources.path(Adwaita, "index.theme") as theme_index_path_:
	theme_index_path = str(theme_index_path_)


class AdwaitaIconTheme(HicolorIconTheme):
	_hicolor_theme: IconTheme = HicolorIconTheme.create()

	@classmethod
	def create(cls):
		"""
		Create an instance of the Adwaita Icon Theme
		"""

		with importlib_resources.path(Adwaita, "index.theme") as theme_index_path_:
			theme_index_path = str(theme_index_path_)

		return cls.from_configparser(theme_index_path)

	def find_icon(
			self,
			icon_name: str,
			size: int,
			scale: Any,
			prefer_this_theme: bool = True,
			) -> Optional[Icon]:
		"""
		Searches for the icon with the given name and size.

		:param icon_name: The name of the icon to find.
			Any `FreeDesktop Icon Theme Specification <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>`_
			name can be used.
		:type icon_name: str
		:param size: The desired size of the icon
		:type size: int
		:param scale: TODO: Currently does nothing
		:param prefer_this_theme: Return an icon from this theme even if it has to be resized,
			rather than a correctly sized icon from the parent theme.
		:type prefer_this_theme:

		:return: The icon if it was found, or None
		:rtype: Icon or None
		"""

		icon = self._do_find_icon(icon_name, size, scale, prefer_this_theme)
		if icon:
			return icon
		else:
			# If we get here we didn't find the icon.
			return self._hicolor_theme.find_icon(icon_name, size, scale)


class wxAdwaitaIconTheme(wxHicolorIconTheme):
	_adwaita_theme: IconTheme = AdwaitaIconTheme.create()

	def CreateBitmap(self, id: Any, client: Any, size: Union[Tuple[int], wx.Size]) -> wx.Bitmap:
		icon = self._adwaita_theme.find_icon(id, size[0], None)

		if icon:
			print(icon, icon.path)
			return self.icon2bitmap(icon, size[0])

		else:
			# return self._humanity_theme.find_icon("image-missing", size[0], None).as_bitmap()
			print("Icon not found in Adwaita theme")
			print(id)
			return super().CreateBitmap(id, client, size)


if __name__ == "__main__":
	# theme = AdwaitaIconTheme.from_configparser(theme_index_path)
	theme = AdwaitaIconTheme.create()

	# for directory in theme.directories:
	# 	print(directory.icons)
	# 3rd party
	from wx_icons_hicolor import test, test_random_icons

	# test_random_icons(theme)
	test.test_icon_theme(theme, show_success=False)
