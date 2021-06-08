defaultPage = """
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="ie=edge" http-equiv="x-ua-compatible"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <link href="/favicon.ico" rel="icon"/>
  <title>
   Assessment Marks
  </title>
  <link href="/libs/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet"/>
  <link href="/vic-ui-kit/css/ecs.bootstrap.css" rel="stylesheet"/>
  <style type="text/css">
   .comment-text {white-space: pre-wrap;}
.panel-heading {
  cursor: pointer;
}
.panel-heading:hover {
  background-color: #d6e9d6;
}
.panel-heading:after {
  font-family: 'Glyphicons Halflings';
  content: "\e114";
  float: right;
  margin-top: -22px;
}
.panel-heading.collapsed:after {
  content: "\e080";
}
.final-mark {
  width: 160px;
}
  </style>
  <script src="/libs/jquery/3.1.1/jquery.min.js">
  </script>
  <script src="/libs/bootstrap/3.3.7/js/bootstrap.min.js">
  </script>
 </head>
 <body>
  <div class="navbar navbar-default" id="global-nav" role="navigation">
   <div class="container">
    <div class="navbar-header">
     <button aria-expanded="false" class="navbar-toggle collapsed" data-target="#top-menu" data-toggle="collapse" type="button">
      <span class="sr-only">
       Toggle navigation
      </span>
      <span class="icon-bar">
      </span>
      <span class="icon-bar">
      </span>
      <span class="icon-bar">
      </span>
     </button>
    </div>
    <div class="collapse navbar-collapse" id="top-menu">
     <ul class="nav navbar-nav" id="vic-links">
      <li>
       <a href="https://www.wgtn.ac.nz">
        <span class="glyphicon glyphicon-home">
        </span>
       </a>
      </li>
      <li>
       <a href="https://www.wgtn.ac.nz/study">
        Future students
       </a>
      </li>
      <li>
       <a href="https://www.wgtn.ac.nz/international">
        International students
       </a>
      </li>
      <li>
       <a href="https://www.wgtn.ac.nz/students">
        Current students
       </a>
      </li>
      <li>
       <a href="https://www.wgtn.ac.nz/research">
        Research
       </a>
      </li>
      <li>
       <a href="https://www.wgtn.ac.nz/about">
        About Victoria
       </a>
      </li>
      <li>
       <a href="/logout?ReturnUrl=https:%2f%2fapps.ecs.vuw.ac.nz%2fcgi-bin%2fstudentmarks">
        Log Out (youngisaa)
       </a>
      </li>
     </ul>
     <ul class="nav navbar-nav navbar-right" id="vic-search">
      <li>
       <form action="https://www.wgtn.ac.nz/search" class="navbar-form collapse" id="search-form" method="get">
        <div class="form-group pull-left" id="global-search">
         <input autocomplete="off" name="q" placeholder="Search for..." required="" type="text"/>
        </div>
        <input type="submit" value="Go"/>
       </form>
      </li>
      <li>
       <a aria-controls="search-form" aria-expanded="false" data-toggle="collapse" href="#search-form" role="button">
        <span class="glyphicon glyphicon-search" id="search-icon">
        </span>
       </a>
      </li>
     </ul>
    </div>
   </div>
  </div>
  <div id="site-header">
   <div class="container">
    <div class="row">
     <div class="col-md-3 hidden-xs hidden-sm" id="logo">
      <a href="https://www.wgtn.ac.nz" title="Victoria University of Wellington homepage">
       <picture>
        <source media="(max-width: 1087px)" srcset="/vic-ui-kit/images/logo-white-full.svg">
         <img alt="Victoria University of Wellington" src="/vic-ui-kit/images/logo-white-full.svg"/>
        </source>
       </picture>
      </a>
     </div>
     <div class="col-md-9" id="site-intro">
      <a href="https://www.wgtn.ac.nz/ecs" title="School of Engineering and Computer Science">
       <h1>
        <span class="preline">
         School of
        </span>
        Engineering and Computer Science
        <small lang="mi">
         Te Kura Mātai Pūkaha, Pūrorohiko
        </small>
       </h1>
      </a>
     </div>
    </div>
   </div>
  </div>
  <div id="app-nav">
   <div class="container">
    <h1>
     Assessment Marks
    </h1>
   </div>
  </div>
  <div id="content">
   <div class="container">
    <div class="pull-right">
     <a href="?current-year=1">
      Show all courses for current year
     </a>
    </div>
    <div class="clearfix">
    </div>
    <ul class="nav nav-tabs" role="tablist">
     <li class="active" role="presentation">
      <a aria-controls="COMP26120211" data-toggle="tab" href="#COMP26120211" role="tab">
       COMP261
      </a>
     </li>
     <li role="presentation">
      <a aria-controls="NWEN24120211" data-toggle="tab" href="#NWEN24120211" role="tab">
       NWEN241
      </a>
     </li>
     <li role="presentation">
      <a aria-controls="SWEN22120211" data-toggle="tab" href="#SWEN22120211" role="tab">
       SWEN221
      </a>
     </li>
    </ul>
    <div class="tab-content">
     <div class="tab-pane active" id="COMP26120211" role="tabpanel">
      <h3 id="">
       COMP261 - Algorithms and Data Structures (2021 T1)
      </h3>
      <h5>
       Submission System Assessments
      </h5>
      <div aria-multiselectable="true" class="panel-group" id="accordionCOMP26120211" role="tablist">
       <div class="panel panel-success">
        <div aria-controls="collapseCOMP26120211Assignment_1" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionCOMP26120211" data-target="#collapseCOMP26120211Assignment_1" data-toggle="collapse" id="headingCOMP26120211Assignment_1" role="tab">
         <h4 class="panel-title">
          Assignment_1
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingCOMP26120211Assignment_1" class="panel-collapse collapse" id="collapseCOMP26120211Assignment_1" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Minimum
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              30 / 30
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Core
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              35 / 35
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Completion
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              20 / 20
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Challenge
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              15 / 15
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Perfect!
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseCOMP26120211Assignment_2" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionCOMP26120211" data-target="#collapseCOMP26120211Assignment_2" data-toggle="collapse" id="headingCOMP26120211Assignment_2" role="tab">
         <h4 class="panel-title">
          Assignment_2
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingCOMP26120211Assignment_2" class="panel-collapse collapse" id="collapseCOMP26120211Assignment_2" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Minimum
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              40 / 40
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Core
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              35 / 35
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Completion
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Challenge
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              15 / 20
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Additional 5 marks for implementing traffic lights.
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseCOMP26120211Test_1" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionCOMP26120211" data-target="#collapseCOMP26120211Test_1" data-toggle="collapse" id="headingCOMP26120211Test_1" role="tab">
         <h4 class="panel-title">
          Test_1
          <span class="pull-right final-mark">
           Final Mark: 35.50
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingCOMP26120211Test_1" class="panel-collapse collapse" id="collapseCOMP26120211Test_1" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Q1
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              25.50 / 30
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Q2
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              35.50 / 40
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseCOMP26120211Assignment_3" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionCOMP26120211" data-target="#collapseCOMP26120211Assignment_3" data-toggle="collapse" id="headingCOMP26120211Assignment_3" role="tab">
         <h4 class="panel-title">
          Assignment_3
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingCOMP26120211Assignment_3" class="panel-collapse collapse" id="collapseCOMP26120211Assignment_3" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Stage 1
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              35 / 35
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Stage 2
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              30 / 30
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Stage 3
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              20 / 20
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Stage 4
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              15 / 15
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Perfect!
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
      </div>
      <br/>
      <h4>
       Automatic late penalties applies to this course
      </h4>
      <table class="table table-bordered table-nonfluid">
       <tr>
        <td>
         <strong>
          3 days
         </strong>
         late submission are allowed for this course.
        </td>
       </tr>
       <tr>
        <td>
         You have
         <strong>
          3 days
         </strong>
         late submission remaining for this course.
        </td>
       </tr>
      </table>
      <h5>
       Assessment submission times
      </h5>
      <table class="table table-striped table-bordered table-hover table-nonfluid">
       <tr>
        <th>
         Assessment
        </th>
        <th>
         Time Late
        </th>
        <th>
         Late Penalty Days
        </th>
       </tr>
       <tr>
        <td>
         Assignment_1
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Assignment_2
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Test_1
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Test_1_Remote_Submissions
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Assignment_3
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Assignment_4
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Test_2_Remote_Submissions
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Assignment_5
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
      </table>
      <small>
       Allowed late days are not used for assessments with a
       <span class="glyphicon glyphicon-star">
       </span>
       next to it.
      </small>
     </div>
     <div class="tab-pane" id="NWEN24120211" role="tabpanel">
      <h3 id="">
       NWEN241 - Systems Programming (2021 T1)
      </h3>
      <h5>
       Submission System Assessments
      </h5>
      <div aria-multiselectable="true" class="panel-group" id="accordionNWEN24120211" role="tablist">
       <div class="panel panel-success">
        <div aria-controls="collapseNWEN24120211Exercise_1" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionNWEN24120211" data-target="#collapseNWEN24120211Exercise_1" data-toggle="collapse" id="headingNWEN24120211Exercise_1" role="tab">
         <h4 class="panel-title">
          Exercise_1
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingNWEN24120211Exercise_1" class="panel-collapse collapse" id="collapseNWEN24120211Exercise_1" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Activity 1
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Activity 2
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Activity 3
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              20 / 20
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Activity 4
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              20 / 20
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Activity 5
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              20 / 20
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Activity 6
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              20 / 20
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseNWEN24120211Quiz_1" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionNWEN24120211" data-target="#collapseNWEN24120211Quiz_1" data-toggle="collapse" id="headingNWEN24120211Quiz_1" role="tab">
         <h4 class="panel-title">
          Quiz_1
          <span class="pull-right final-mark">
           Final Mark: 40.33
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingNWEN24120211Quiz_1" class="panel-collapse collapse" id="collapseNWEN24120211Quiz_1" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Total Points
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              40.33 / 50
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              40.33 / 50
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseNWEN24120211Assignment_1" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionNWEN24120211" data-target="#collapseNWEN24120211Assignment_1" data-toggle="collapse" id="headingNWEN24120211Assignment_1" role="tab">
         <h4 class="panel-title">
          Assignment_1
          <span class="pull-right final-mark">
           Final Mark: 99
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingNWEN24120211Assignment_1" class="panel-collapse collapse" id="collapseNWEN24120211Assignment_1" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Compilation
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Comments
            </td>
            <td>
             Descriptive, concise and appropriate comments
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Coding Style
            </td>
            <td>
             Completely consistent and clean
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 1 Correctness
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              20 / 20
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 2 Correctness
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              25 / 25
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 3 Correctness
            </td>
            <td>
             See feedback file to see marking details
            </td>
            <td>
             <span class="pull-right">
              14 / 15
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 4 Correctness
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              99 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Please see youngisaa.txt under Feedback files for more comments.
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             Feedback files
            </th>
           </tr>
           <tr>
            <td>
             <a href="?rm=download_file&amp;course=NWEN241&amp;year=2021&amp;trimester=1&amp;assignment=Assignment_1&amp;filename=youngisaa.txt">
              youngisaa.txt
             </a>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseNWEN24120211Exercise_2" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionNWEN24120211" data-target="#collapseNWEN24120211Exercise_2" data-toggle="collapse" id="headingNWEN24120211Exercise_2" role="tab">
         <h4 class="panel-title">
          Exercise_2
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingNWEN24120211Exercise_2" class="panel-collapse collapse" id="collapseNWEN24120211Exercise_2" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Activity 1
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              50 / 50
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Activity 2
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              15 / 15
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Activity 3
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Activity 4
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              25 / 25
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseNWEN24120211Assignment_2" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionNWEN24120211" data-target="#collapseNWEN24120211Assignment_2" data-toggle="collapse" id="headingNWEN24120211Assignment_2" role="tab">
         <h4 class="panel-title">
          Assignment_2
          <span class="pull-right final-mark">
           Final Mark: 95
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingNWEN24120211Assignment_2" class="panel-collapse collapse" id="collapseNWEN24120211Assignment_2" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Compilation
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Comments
            </td>
            <td>
             Comments are relevant and descriptive
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Coding Style
            </td>
            <td>
             Code is consistent and clean, easy to follow.
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 1 Correctness
            </td>
            <td>
             See feedback file to see marking details
             <br/>
             <br/>
             Had to add '\n' to make the code pass the test cases.
            </td>
            <td>
             <span class="pull-right">
              40 / 45
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 2 Correctness
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              15 / 15
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 3 Correctness
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              95 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Please see youngisaa.txt under Feedback files for more comments.
            </td>
           </tr>
           <tr>
            <td class="comment-text">
             Well done
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             Feedback files
            </th>
           </tr>
           <tr>
            <td>
             <a href="?rm=download_file&amp;course=NWEN241&amp;year=2021&amp;trimester=1&amp;assignment=Assignment_2&amp;filename=youngisaa.txt">
              youngisaa.txt
             </a>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseNWEN24120211Quiz_2" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionNWEN24120211" data-target="#collapseNWEN24120211Quiz_2" data-toggle="collapse" id="headingNWEN24120211Quiz_2" role="tab">
         <h4 class="panel-title">
          Quiz_2
          <span class="pull-right final-mark">
           Final Mark: 48
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingNWEN24120211Quiz_2" class="panel-collapse collapse" id="collapseNWEN24120211Quiz_2" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Total Points
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              48 / 50
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              48 / 50
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseNWEN24120211Assignment_3" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionNWEN24120211" data-target="#collapseNWEN24120211Assignment_3" data-toggle="collapse" id="headingNWEN24120211Assignment_3" role="tab">
         <h4 class="panel-title">
          Assignment_3
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingNWEN24120211Assignment_3" class="panel-collapse collapse" id="collapseNWEN24120211Assignment_3" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Compilation
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Comments
            </td>
            <td>
             Great commenting, all relevant &amp; descriptive.
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Coding Style
            </td>
            <td>
             Code is clean and consistent, very easy to follow
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 1 Correctness
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              45 / 45
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 2 Correctness
            </td>
            <td>
             See feedback file to see marking details
            </td>
            <td>
             <span class="pull-right">
              15 / 15
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Task 3 Correctness
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              10 / 10
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Please see youngisaa.txt under Feedback files for more comments.
            </td>
           </tr>
           <tr>
            <td class="comment-text">
             Fantastic work!
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             Feedback files
            </th>
           </tr>
           <tr>
            <td>
             <a href="?rm=download_file&amp;course=NWEN241&amp;year=2021&amp;trimester=1&amp;assignment=Assignment_3&amp;filename=youngisaa.txt">
              youngisaa.txt
             </a>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
      </div>
      <br/>
      <h4>
       Automatic late penalties applies to this course
      </h4>
      <table class="table table-bordered table-nonfluid">
       <tr>
        <td>
         <strong>
          3 days
         </strong>
         late submission are allowed for this course.
        </td>
       </tr>
       <tr>
        <td>
         You have
         <strong>
          2 days, 8 hours, and 31 minutes
         </strong>
         late submission remaining for this course.
        </td>
       </tr>
      </table>
      <h5>
       Assessment submission times
      </h5>
      <table class="table table-striped table-bordered table-hover table-nonfluid">
       <tr>
        <th>
         Assessment
        </th>
        <th>
         Time Late
        </th>
        <th>
         Late Penalty Days
        </th>
       </tr>
       <tr>
        <td>
         Exercise_1
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Quiz_1
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Assignment_1
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Exercise_2
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Assignment_2
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Quiz_2
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Exercise_3
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Assignment_3
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Exercise_4
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Assignment_4
        </td>
        <td>
         15 hours, 28 minutes, and 59 seconds
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Final_Test_for_Remote_Students
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
      </table>
      <small>
       Allowed late days are not used for assessments with a
       <span class="glyphicon glyphicon-star">
       </span>
       next to it.
      </small>
     </div>
     <div class="tab-pane" id="SWEN22120211" role="tabpanel">
      <h3 id="">
       SWEN221 - Software Development (2021 T1)
      </h3>
      <h5>
       Submission System Assessments
      </h5>
      <div aria-multiselectable="true" class="panel-group" id="accordionSWEN22120211" role="tablist">
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_1" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_1" data-toggle="collapse" id="headingSWEN22120211Lab_1" role="tab">
         <h4 class="panel-title">
          Lab_1
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_1" class="panel-collapse collapse" id="collapseSWEN22120211Lab_1" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_2" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_2" data-toggle="collapse" id="headingSWEN22120211Lab_2" role="tab">
         <h4 class="panel-title">
          Lab_2
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_2" class="panel-collapse collapse" id="collapseSWEN22120211Lab_2" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_3" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_3" data-toggle="collapse" id="headingSWEN22120211Lab_3" role="tab">
         <h4 class="panel-title">
          Lab_3
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_3" class="panel-collapse collapse" id="collapseSWEN22120211Lab_3" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Assignment_1" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Assignment_1" data-toggle="collapse" id="headingSWEN22120211Assignment_1" role="tab">
         <h4 class="panel-title">
          Assignment_1
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Assignment_1" class="panel-collapse collapse" id="collapseSWEN22120211Assignment_1" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Division of Concepts into Classes
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Division of Work into Methods
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Use of Names
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Use of JavaDoc Comments
            </td>
            <td>
             Great work on the javadocs
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Use of Other Comments
            </td>
            <td>
             Excellent use of comments
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Overall Consistency
            </td>
            <td>
             Good consistency and use of white space especially to make your code more readable
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_1
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_2
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_3
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_4
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Awesome job on this assignment, good luck for assignment 2
            </td>
           </tr>
           <tr>
            <td class="comment-text">
             Please see automark_output.txt under Feedback files for more comments.
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             Feedback files
            </th>
           </tr>
           <tr>
            <td>
             <a href="?rm=download_file&amp;course=SWEN221&amp;year=2021&amp;trimester=1&amp;assignment=Assignment_1&amp;filename=automark_output.txt">
              automark_output.txt
             </a>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_4" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_4" data-toggle="collapse" id="headingSWEN22120211Lab_4" role="tab">
         <h4 class="panel-title">
          Lab_4
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_4" class="panel-collapse collapse" id="collapseSWEN22120211Lab_4" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_5" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_5" data-toggle="collapse" id="headingSWEN22120211Lab_5" role="tab">
         <h4 class="panel-title">
          Lab_5
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_5" class="panel-collapse collapse" id="collapseSWEN22120211Lab_5" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Assignment_2" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Assignment_2" data-toggle="collapse" id="headingSWEN22120211Assignment_2" role="tab">
         <h4 class="panel-title">
          Assignment_2
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Assignment_2" class="panel-collapse collapse" id="collapseSWEN22120211Assignment_2" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Division of Concepts into Classes
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Division of Work into Methods
            </td>
            <td>
             Good division of work into methods!
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Use of Names
            </td>
            <td>
             excellent names
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Use of JavaDoc Comments
            </td>
            <td>
             Really great job on the javadoc comments. A couple missed in Tetromino class but negligible.
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Use of Other Comments
            </td>
            <td>
             Good use of other comments.
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Overall Consistency
            </td>
            <td>
             Great overall consistency.
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_1
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_2
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_3
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_4
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Great job! Highly recommend turning on javadoc warnings in the IDE to those last few javadoc errors.
             <br/>
            </td>
           </tr>
           <tr>
            <td class="comment-text">
             Please see automark_output.txt under Feedback files for more comments.
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             Feedback files
            </th>
           </tr>
           <tr>
            <td>
             <a href="?rm=download_file&amp;course=SWEN221&amp;year=2021&amp;trimester=1&amp;assignment=Assignment_2&amp;filename=automark_output.txt">
              automark_output.txt
             </a>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Test_1" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Test_1" data-toggle="collapse" id="headingSWEN22120211Test_1" role="tab">
         <h4 class="panel-title">
          Test_1
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Test_1" class="panel-collapse collapse" id="collapseSWEN22120211Test_1" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Part_1
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_2
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_3
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_4
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_5
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_6
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Please see automark_output.txt under Feedback files for more comments.
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             Feedback files
            </th>
           </tr>
           <tr>
            <td>
             <a href="?rm=download_file&amp;course=SWEN221&amp;year=2021&amp;trimester=1&amp;assignment=Test_1&amp;filename=automark_output.txt">
              automark_output.txt
             </a>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_6" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_6" data-toggle="collapse" id="headingSWEN22120211Lab_6" role="tab">
         <h4 class="panel-title">
          Lab_6
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_6" class="panel-collapse collapse" id="collapseSWEN22120211Lab_6" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_7" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_7" data-toggle="collapse" id="headingSWEN22120211Lab_7" role="tab">
         <h4 class="panel-title">
          Lab_7
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_7" class="panel-collapse collapse" id="collapseSWEN22120211Lab_7" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Assignment_3" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Assignment_3" data-toggle="collapse" id="headingSWEN22120211Assignment_3" role="tab">
         <h4 class="panel-title">
          Assignment_3
          <span class="pull-right final-mark">
           Final Mark: 99.40
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Assignment_3" class="panel-collapse collapse" id="collapseSWEN22120211Assignment_3" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Use of Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Comments
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_1
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_2
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_3
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              96.40 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Coverage
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              99.40 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Great commenting and use of tests :)
            </td>
           </tr>
           <tr>
            <td class="comment-text">
             Please see automark_output.txt under Feedback files for more comments.
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             Feedback files
            </th>
           </tr>
           <tr>
            <td>
             <a href="?rm=download_file&amp;course=SWEN221&amp;year=2021&amp;trimester=1&amp;assignment=Assignment_3&amp;filename=automark_output.txt">
              automark_output.txt
             </a>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_8" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_8" data-toggle="collapse" id="headingSWEN22120211Lab_8" role="tab">
         <h4 class="panel-title">
          Lab_8
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_8" class="panel-collapse collapse" id="collapseSWEN22120211Lab_8" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Test_2" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Test_2" data-toggle="collapse" id="headingSWEN22120211Test_2" role="tab">
         <h4 class="panel-title">
          Test_2
          <span class="pull-right final-mark">
           Final Mark: 100
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Test_2" class="panel-collapse collapse" id="collapseSWEN22120211Test_2" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Total
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              16 / 16
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_9" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_9" data-toggle="collapse" id="headingSWEN22120211Lab_9" role="tab">
         <h4 class="panel-title">
          Lab_9
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_9" class="panel-collapse collapse" id="collapseSWEN22120211Lab_9" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Assignment_4" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Assignment_4" data-toggle="collapse" id="headingSWEN22120211Assignment_4" role="tab">
         <h4 class="panel-title">
          Assignment_4
          <span class="pull-right final-mark">
           Final Mark: 99.83
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Assignment_4" class="panel-collapse collapse" id="collapseSWEN22120211Assignment_4" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Division of Concepts into Classes
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Division of Work into Methods
            </td>
            <td>
             You could have split the code more in your computer player methods but overall there is a good effort to divide the methods up
            </td>
            <td>
             <span class="pull-right">
              4.5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Use of Names
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Use of JavaDoc Comments
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Use of Other Comments
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Overall Consistency
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              5 / 5
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_1
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_2
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_3
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Part_4
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              99.83 / 100
             </span>
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             General comments
            </th>
           </tr>
           <tr>
            <td class="comment-text">
             Please see automark_output.txt under Feedback files for more comments.
            </td>
           </tr>
          </table>
          <table class="table table-striped table-bordered">
           <tr>
            <th>
             Feedback files
            </th>
           </tr>
           <tr>
            <td>
             <a href="?rm=download_file&amp;course=SWEN221&amp;year=2021&amp;trimester=1&amp;assignment=Assignment_4&amp;filename=automark_output.txt">
              automark_output.txt
             </a>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
       <div class="panel panel-success">
        <div aria-controls="collapseSWEN22120211Lab_10" aria-expanded="true" class="panel-heading collapsed" data-parent="#accordionSWEN22120211" data-target="#collapseSWEN22120211Lab_10" data-toggle="collapse" id="headingSWEN22120211Lab_10" role="tab">
         <h4 class="panel-title">
          Lab_10
          <span class="pull-right final-mark">
           Final Mark: 100.0
          </span>
         </h4>
        </div>
        <div aria-labelledby="headingSWEN22120211Lab_10" class="panel-collapse collapse" id="collapseSWEN22120211Lab_10" role="tabpanel">
         <div class="panel-body">
          <table class="table table-striped table-bordered table-nonfluid">
           <tr>
            <th>
             Question
            </th>
            <th>
             Comment
            </th>
            <th class="col-md-1">
             Mark
            </th>
           </tr>
           <tr>
            <td>
             Tests
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
           <tr>
            <td>
             Final
            </td>
            <td>
            </td>
            <td>
             <span class="pull-right">
              100.0 / 100
             </span>
            </td>
           </tr>
          </table>
         </div>
        </div>
       </div>
      </div>
      <br/>
      <h4>
       Automatic late penalties applies to this course
      </h4>
      <table class="table table-bordered table-nonfluid">
       <tr>
        <td>
         <strong>
          3 days
         </strong>
         late submission are allowed for this course.
        </td>
       </tr>
       <tr>
        <td>
         You have
         <strong>
          2 hours, 47 minutes, and 23 seconds
         </strong>
         late submission remaining for this course.
        </td>
       </tr>
      </table>
      <h5>
       Assessment submission times
      </h5>
      <table class="table table-striped table-bordered table-hover table-nonfluid">
       <tr>
        <th>
         Assessment
        </th>
        <th>
         Time Late
        </th>
        <th>
         Late Penalty Days
        </th>
       </tr>
       <tr>
        <td>
         Lab_1
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Lab_2
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Lab_3
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Assignment_1
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Lab_4
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Lab_5
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Assignment_2
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Test_1
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Lab_6
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Lab_7
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Assignment_3
        </td>
        <td>
         2 days, 21 hours, and 13 minutes
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Lab_8
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Test_2
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Lab_9
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
       <tr>
        <td>
         Assignment_4
        </td>
        <td>
         Not late
        </td>
        <td>
         None
        </td>
       </tr>
       <tr>
        <td>
         Lab_10
        </td>
        <td>
         Not late
        </td>
        <td>
         None
         <span class="glyphicon glyphicon-star">
         </span>
        </td>
       </tr>
      </table>
      <small>
       Allowed late days are not used for assessments with a
       <span class="glyphicon glyphicon-star">
       </span>
       next to it.
      </small>
     </div>
    </div>
    <script type="text/javascript">
     $(document).ready(function() {
  var show_lines = 20;
  $('.comment-text').each(function() {
    var comment = $(this).html();
    var line_count = (comment.match(/<br>/g) || []).length

    if(line_count > show_lines) {
      var pos = find_index_n(comment, '<br>', show_lines);
      var show_text = comment.substr(0, pos);
      var hidden_text = comment.substr(pos, comment.length - pos);

      var comment_html = show_text + '<a class="more pull-right">show more</a><span class="hidden-text hidden">' + hidden_text + '<a class="less pull-right">show less</a></span>';

      $(this).html(comment_html);
    }
  });

  $(".more").click(function(){
    $(this).addClass("hidden");
    $(this).parent().find(".hidden-text").removeClass("hidden");
  });

  $(".less").click(function(){
    $(this).parent().addClass("hidden");
    $(this).closest(".comment-text").find(".more").removeClass("hidden");
  });
});

function find_index_n(str, pat, n) {
  var pos = 0;
  while(n) {
    pos = str.indexOf(pat, pos) + 1;
    n--;
  }
  return pos-1;
}
    </script>
   </div>
  </div>
  <footer id="footer">
   <div class="container">
    <div class="row">
     <div class="pull-left">
      <a href="https://www.wgtn.ac.nz/site-info" title="Site info">
       Site info
      </a>
      <a href="https://www.wgtn.ac.nz/site-info/site-map" title="Site map">
       Site map
      </a>
      <a href="https://www.wgtn.ac.nz/site-info/feedback" title="Feedback">
       Feedback
      </a>
      <a href="https://www.wgtn.ac.nz/site-info/glossary" title="Glossary">
       Glossary
      </a>
     </div>
     <div class="pull-right">
      <span>
       Copyright © Victoria University of Wellington, New Zealand
      </span>
     </div>
    </div>
   </div>
  </footer>
  <script>
   var vic_search_form = $('#search-form');
vic_search_form.on('hide.bs.collapse', function () {
  $("#search-icon").removeClass("glyphicon-remove").addClass("glyphicon-search");
});
vic_search_form.on('show.bs.collapse', function () {
  $("#search-icon").removeClass("glyphicon-search").addClass("glyphicon-remove");
});
  </script>
 </body>
</html>"""
