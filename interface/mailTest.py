# http://www.runoob.com/python/python-email.html

import smtplib
from datetime import datetime as dt
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = '464625206@qq.com'  # 发件人邮箱账号
password = '****'  # 发件人邮箱密码
receiver = ['464625206@qq.com']  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


def send_mail():

    # 读取测试报告内容
    with open(report_file, 'r', encoding='UTF-8') as f:
        content = f.read()

    msg = MIMEMultipart('mixed')

    # 添加邮件内容
    msg_html = MIMEText(content, 'html', 'utf-8')
    msg.attach(msg_html)

    # 添加附件
    msg_attachment = MIMEText(content, 'html', 'utf-8')
    msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format(report_file)
    msg.attach(msg_attachment)

    msg['Subject'] = mail_subjet
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    try:
        # 连接邮件服务器
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        # 登陆
        s.login(sender, password)
        # 发送邮件
        s.sendmail(sender, receiver, msg.as_string())
        # 退出
        s.quit()
    except Exception as e:
        print("Exceptioin ", e)


if __name__ == '__main__':
    # ret = mail()
    # if ret:
    #     print("邮件发送成功")
    # else:
    #     print("邮件发送失败")

    # 邮件标题
    mail_subjet = u'NoseTests_测试报告_{0}'.format(dt.now().strftime('%Y%m%d'))

    # 测试报告名称
    report_file = 'TestReport.html'

    # 运行nosetests进行自动化测试并生成测试报告
    print('Run Nosetests Now...')
    # os.system('nosetests -v {0} --with-html --html-file={1}'.format(__file__, report_file))

    # 发送测试报告邮件
    print('Send Test Report Mail Now...')
    send_mail()
