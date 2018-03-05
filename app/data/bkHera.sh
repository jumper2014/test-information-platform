#!/bin/bash
mysqldump -uroot -prootPass hera | gzip > /root/mysql_backup/hera_$(date +%Y%m%d_%H%M%S).sql.gz

