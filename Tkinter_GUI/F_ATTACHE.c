
#include <stdio.h>
#include <string.h>
#include <curl/curl.h>

#define FROM "<raspberry.localhost@gmail.com>"
#define TO "<maxmaxou1713@gmail.com>"
#define CC "<maxence.bonnici2002@gmail.com>"

static const char *headers_text[] = {
  "Date: ",
  "To: " TO " (Destinataire Princ.)",
  "From: " FROM " (raspberry_de_maxence)",
  "Cc: " CC " (Destinataires CC)",
  "Message-ID: ",
  "Subject:!!! ⚠️  ALERTE ROUGE ⚠️  !!! ",
  NULL
};

static const char inline_html[] =

  "<html><body>\r\n"
  "<p>La <b>BATTERIE</b> est bientôt à plat !</p>"
  "<p>☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠<p>"
  "<a href=https://f3xbpyopakiqguagzn8lyw.on.drv.tw/rasp.html><u>Notre Site</u></a>"
  "<br />\r\n"
  "</body></html>\r\n";

int main() {
  CURL *curl;
  CURLcode res = CURLE_OK;
  curl = curl_easy_init();
  if(curl) {
    struct curl_slist *headers = NULL;
    struct curl_slist *recipients = NULL;
    struct curl_slist *slist = NULL;
    curl_mime *mime;
    curl_mime *alt;
    curl_mimepart *part;
    const char **cpp;
    curl_easy_setopt(curl, CURLOPT_URL, "smtps://smtp.gmail.com:465");
    curl_easy_setopt(curl, CURLOPT_USERPWD, "raspberry.localhost@gmail.com:123azert");
    curl_easy_setopt(curl, CURLOPT_USERAGENT, "curl/7.77.0");
    curl_easy_setopt(curl, CURLOPT_MAXREDIRS, 50L);
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0L);
    curl_easy_setopt(curl, CURLOPT_USE_SSL, (long)CURLUSESSL_ALL);
    curl_easy_setopt(curl, CURLOPT_TCP_KEEPALIVE, 1L);
    curl_easy_setopt(curl, CURLOPT_MAIL_RCPT, recipients);
    curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
    curl_easy_setopt(curl, CURLOPT_MAIL_FROM, FROM);
    recipients = curl_slist_append(recipients, TO);
    recipients = curl_slist_append(recipients, CC);
    curl_easy_setopt(curl, CURLOPT_MAIL_RCPT, recipients);

    for(cpp = headers_text; *cpp; cpp++)
      headers = curl_slist_append(headers, *cpp);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    mime = curl_mime_init(curl);
    alt = curl_mime_init(curl);
    part = curl_mime_addpart(alt);
    curl_mime_data(part, inline_html, CURL_ZERO_TERMINATED);
    curl_mime_type(part, "text/html");
    part = curl_mime_addpart(alt);
    part = curl_mime_addpart(mime);
    curl_mime_subparts(part, alt);
    curl_mime_headers(part, slist, 1);
    part = curl_mime_addpart(mime);
    curl_mime_filedata(part, "log.txt");
    curl_easy_setopt(curl, CURLOPT_MIMEPOST, mime);
    res = curl_easy_perform(curl);
        if(res != CURLE_OK)
      fprintf(stderr, "curl_easy_perform() failed: %s\n",
          curl_easy_strerror(res));
    curl_slist_free_all(recipients);
    curl_slist_free_all(headers);
    curl_easy_cleanup(curl);
    curl_mime_free(mime);
  }
  return 0;
}
