# Copyright 2012 Globo.com. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
