#!/usr/bin/env python
#
#  __init__.py
"""
Adwaita icon theme for wxPython.
"""
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
from typing import Any, Optional, Tuple, Type, Union

# 3rd party
import wx  # type: ignore[import-not-found]
from domdf_python_tools.compat import importlib_resources
from domdf_python_tools.doctools import prettify_docstrings
from wx_icons_hicolor import HicolorIconTheme, wxHicolorIconTheme
from wx_icons_hicolor.icon import Icon
from wx_icons_hicolor.icon_theme import IconTheme

# this package
from wx_icons_adwaita import Adwaita

__all__ = ["AdwaitaIconTheme", "version", "wxAdwaitaIconTheme"]

__version__: str = "0.2.0"


def version() -> str:
	"""
	Returns the version of this package and the icon theme, formatted for printing.
	"""

	return f"""wx_icons_adwaita
Version {__version__}
Adwaita Icon Theme Version 3.28.0
"""


with importlib_resources.path(Adwaita, "index.theme") as theme_index_path_:
	theme_index_path = str(theme_index_path_)


@prettify_docstrings
class AdwaitaIconTheme(HicolorIconTheme):
	"""
	The Adwaita Icon Theme.

	:param name: short name of the icon theme, used in e.g. lists when selecting themes.
	:param comment: longer string describing the theme
	:param inherits: The name of the theme that this theme inherits from. If an icon name is not found
		in the current theme, it is searched for in the inherited theme (and recursively in all the
		inherited themes).

		If no theme is specified implementations are required to add the "hicolor" theme to the
		inheritance tree. An implementation may optionally add other default themes in between the last
		specified theme and the hicolor theme.
	:param directories: list of subdirectories for this theme. For every subdirectory there
		must be a section in the index.theme file describing that directory.
	:param scaled_directories: Additional list of subdirectories for this theme, in addition to the ones
		in Directories. These directories should only be read by implementations supporting scaled
		directories and was added to keep compatibility with old implementations that don't support these.
	:param hidden: Whether to hide the theme in a theme selection user interface. This is used for things
		such as fallback-themes that are not supposed to be visible to the user.
	:param example: The name of an icon that should be used as an example of how this theme looks.
	"""

	_hicolor_theme: IconTheme = HicolorIconTheme.create()

	@classmethod
	def create(cls: Type["AdwaitaIconTheme"]) -> "AdwaitaIconTheme":
		"""
		Create an instance of the Adwaita Icon Theme.
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
			Any `FreeDesktop Icon Theme Specification
			<https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>`_
			name can be used.
		:param size: The desired size of the icon
		:param scale: TODO: Currently does nothing
		:param prefer_this_theme: Return an icon from this theme even if it has to be resized,
			rather than a correctly sized icon from the parent theme.

		:return: The icon if it was found, or :py:obj:`None`.
		"""

		icon = self._do_find_icon(icon_name, size, scale, prefer_this_theme)
		if icon:
			return icon
		else:
			# If we get here we didn't find the icon.
			return self._hicolor_theme.find_icon(icon_name, size, scale)


@prettify_docstrings
class wxAdwaitaIconTheme(wxHicolorIconTheme):
	"""
	:class:`wx.ArtProvider` subclass providing the Adwaita Icon Theme.
	"""

	_adwaita_theme: IconTheme = AdwaitaIconTheme.create()

	def CreateBitmap(
			self,
			id: Any,  # noqa: A002  # pylint: disable=redefined-builtin
			client: Any,
			size: Union[Tuple[int], wx.Size],
			) -> wx.Bitmap:
		"""
		Returns the requested resource.

		:param id: Unique identifier of the bitmap.
		:param client: Identifier of the client (i.e. who is asking for the bitmap). This only serves as a hint.
		:param size: Preferred size of the bitmap. The function may return a bitmap of different dimensions;
			it will be automatically rescaled to meet client’s request.
		"""

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
	# from wx_icons_hicolor import test, test_random_icons
	from wx_icons_hicolor import test

	# test_random_icons(theme)
	test.test_icon_theme(theme, show_success=False)
